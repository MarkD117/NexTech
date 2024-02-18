from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        # Assigning request as an attribute of the class if we need 
        # access to any attributes of the request coming from stripe.
        self.request = request
    
    # private method
    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        # Render email text files to strings
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        # Send mail with specified parameters
        send_mail(
            subject,
            body,
            # Send email from
            settings.DEFAULT_FROM_EMAIL,
            # Send email to
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Get payment intent
        intent = event.data.object
        # Get info from intent metadata
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean the data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        # Profile set to None so we can still allow anonymous users to checkout
        profile = None
        username = intent.metadata.username
        # If the username is not 'AnonymousUser' the user is authenticated
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            # Add default info f user has saved
            # info box checked (from metadata)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()
        
        order_exists = False
        attempt = 1
        # While loop runs giving the webhook 5 attempts to
        # find the existing order, if it cannot find one
        # after 5 attempts, the order will be created
        # automatically by the webhook. This allows the
        # view time to submit the form and create the order.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
                
            except Order.DoesNotExist:
                # If order does not exist, attempt increments by 1.
                # Then pythons time module sleeps for 1 second
                attempt += 1
                time.sleep(1)
        if order_exists:
            # Send confirmation email before returning response to Stripe
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                # Create form using data from payment intent
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                # cart is loaded from the json version in the
                # payment intent instead of from the session.
                # Code copied from checkout view.
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            # If anything goes wrong, the order will be deleted if
            # one was created and return 500 server error response
            # to Stripe. This will cause Stripe to automatically
            # try the webhook again later.
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Send confirmation email before returning response to Stripe
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
