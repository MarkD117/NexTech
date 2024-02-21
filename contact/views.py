from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm, ContactForm


def subscribe(request):
    """ This view handles subscribing to the newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully signed up to newsletter!')
            return redirect('home')
        else:
            messages.error(
                request,
                'You have already signed up to our newsletter!'
            )
            return redirect('home')
    else:
        return redirect('home')


def contact(request):
    """ This view handles submitting the contact form """
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
