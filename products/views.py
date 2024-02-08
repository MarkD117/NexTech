from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductCategory


def all_products(request):
    """ This view shows all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        # If a category is submitted
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = ProductCategory.objects.filter(name__in=categories)
        
        # If search is submitted
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any seach criteria!")
                return redirect(reverse('products'))
            
            # Allowing queries to be filtered based on name OR description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This view shows each individual products details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)