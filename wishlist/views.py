from django.shortcuts import render, redirect
from .models import WishList
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    # Retrieve the wishlist of the current user
    wishlist = WishList.objects.get(user=request.user)

    context = {
        'wishlist': wishlist
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist = WishList.objects.get(user=request.user)
    wishlist.products.remove(product)
    return redirect('product_detail', product_id=product_id)