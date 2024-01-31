from django.shortcuts import render


# Create your views here.
def home(request) :
    return render(request, 'mrreporting/home.html')

def about(request) :
    return render(request, 'mrreporting/about.html')


def contact(request) :
    return render(request, 'mrreporting/contact.html')


def modules(request) :
    return render(request, 'mrreporting/modules.html')
