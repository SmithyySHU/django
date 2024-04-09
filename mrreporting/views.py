from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Module, Registration, Course
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

class ModuleDetailView(DetailView):
    model = Module
    
    def get_object(self, queryset=None):
        code = self.kwargs['code']
        return get_object_or_404(Module, code=code)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
    
        module = self.get_object()

    
        is_registered, registration = user_is_registered_for_module(self.request.user, module)
        context['is_registered'] = is_registered        
        context['registration'] = registration          
        

        return context
    
    
    
    
def user_is_registered_for_module(user, module):
    
    if isinstance(user, AnonymousUser) or not user.is_authenticated:
        return False, None
    
    registration = Registration.objects.filter(user=user, module=module).first()
    return registration is not None, registration

@login_required
def register_for_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
               
            registration = form.save(commit=False)
            registration.module = module   
            registration.user = request.user 
                          
            registration.save()
            messages.success(request, f'You have been registered!')    
            

               
            return redirect('mrreporting:module', code=module.code)
        else:
            print(f"Form Errors: {form.errors}")
            messages.warning(request, 'Unable to register!')           
    else:
        form = RegistrationForm()
           
    return redirect('mrreporting:module', code=module.code)


    
@login_required
def remove_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    
    if request.user == registration.user:
        registration.delete()
        messages.success(request, f'Your registration has been removed!') 

    return redirect('mrreporting:module', code=registration.module.code)

def course(request):
    courses = Course.objects.all()
    for course in courses:
        print(f"Course: {course.name}")
        for module in course.allowed_modules.all():
            print(f"Module: {module.name}")
    return render(request, 'mrreporting/course.html', {'courses': courses})