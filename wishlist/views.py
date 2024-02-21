from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishList
from products.models import Product


@login_required
def view_wishlist(request):
    """ This view gets wishlisted items and sends them to the template. """
    try:
        # Try to retrieve the wishlist of the current user
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        # If wishlist doesn't exist for the user, create a new one
        wishlist = WishList.objects.create(user=request.user)

    context = {
        'wishlist': wishlist
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ This view handles adding products to the wishlist """
    product = Product.objects.get(id=product_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, 'Prouct added to Wishlist!')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """ This view handles removing products to the wishlist """
    product = Product.objects.get(id=product_id)
    wishlist = WishList.objects.get(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, 'Prouct removed from Wishlist!')
    return redirect('product_detail', product_id=product_id)
