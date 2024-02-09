from django.shortcuts import render, redirect


def view_cart(request):
    """ This view renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ This view adds a desired quantity of the
        specified product to the shopping cart """

    # Get quantity and redirect url from form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
   # get or create empty cart dictionary
    cart = request.session.get('cart', {})


    # If item already in cart, increment quantity
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    # Add item to bag
    else:
        cart[item_id] = quantity

    # overwriting cart variable in session
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)