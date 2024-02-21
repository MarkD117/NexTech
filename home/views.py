from django.shortcuts import render


def index(request):
    """ This view returns the index page """

    context = {
        'is_home_page': True
    }

    return render(request, 'home/index.html', context)
