from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ This view renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ This view adds a desired quantity of the
        specified product to the shopping cart """

    # Getting product for messages
    product = get_object_or_404(Product, pk=item_id)
    # Get quantity and redirect url from form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
   # get or create empty cart dictionary
    cart = request.session.get('cart', {})


    # If item already in cart, increment quantity
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    # Add item to cart
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    # overwriting cart variable in session
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ This view updates the quantity of the 
        selected product to the specified amount """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})


    if quantity > 0:
        # Set quantity value to updated quantity
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        # Removes item entirely by using pop function
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_cart_item(request, item_id):
    """ This view handles the removal of cart items """
    # Try except block to catch errors
    try:
        # Gets product to be deleted and pops out of cart session
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    
    # return any errors
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
