from django.shortcuts import render
from .models import Module
from .models import Course


# Create your views here.
def home(request) :
    return render(request, 'mrreporting/home.html', {'title' : 'Welcome'})

def about(request) :
    return render(request, 'mrreporting/about.html', {'title' : 'About Us'})


def contact(request) :
    return render(request, 'mrreporting/contact.html', {'title' : 'Contact Us'})


def module(request):
    module_pull = {'modules': Module.objects.all(), 'title': 'Module List'}
    return render(request, 'mrreporting/modules.html', module_pull)

def course(request):
    course_pull = {'course': Course.objects.all(), 'title': 'Course List'}
    return render(request, 'mrreporting/course.html', course_pull)
