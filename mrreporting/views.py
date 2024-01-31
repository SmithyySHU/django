from django.shortcuts import render


# Create your views here.
def home(request) :
    return render(request, 'mrreporting/home.html', {'title' : 'Welcome'})

def about(request) :
    return render(request, 'mrreporting/about.html', {'title' : 'About Us'})


def contact(request) :
    return render(request, 'mrreporting/contact.html', {'title' : 'Contact Us'})


def modules(request) :
    return render(request, 'mrreporting/modules.html', {'title' : 'Modules'})
