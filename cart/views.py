from django.shortcuts import render


def view_cart(request):
    """ This view renders the cart contents page """

    return render(request, 'cart/cart.html')