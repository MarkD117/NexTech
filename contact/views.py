from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully signed up to newsletter!')
            return redirect('home')
    else:
        form = NewsletterForm()

    context = {
        'form': form
    }

    return render(request, 'base.html', context)