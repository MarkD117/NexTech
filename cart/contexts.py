from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # Creates a list of cart items from the cart session variable
    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        # Product object is added to give access to other
        # product fields such as product.image etc
        cart_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })


    # Calculate delivery under threshold
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_target = settings.FREE_DELIVERY_THRESHOLD - total
    # Sets delivery to 0 if total is over threshold
    else:
        delivery = 0
        free_delivery_target = 0
    
    grand_total = delivery + total
    
    # Add all items to context for use in templates across the site
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_target': free_delivery_target,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context