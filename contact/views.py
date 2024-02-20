from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm, ContactForm


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully signed up to newsletter!')
            return redirect('home')
        else:
            messages.error(
                request,
                'Uh oh! Looks like you entered an invalid email address '
                'or you have already signed up to our newsletter!'
            )
            return redirect('home')
    else:
        return redirect('home')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent to the team!')
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'ContactForm': form
    }

    return render(request, 'contact/contact.html', context)