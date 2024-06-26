from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, FormView
from .models import Module, Registration, Course
from .forms import RegistrationForm, ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage



# Create your views here.
def home(request) :
    return render(request, 'mrreporting/home.html', {'title' : 'Welcome'})

def about(request) :
    return render(request, 'mrreporting/about.html', {'title' : 'About Us'})


#def contact(request) :
 ##   return render(request, 'mrreporting/contact.html', {'title' : 'Contact Us'})


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

class CourseDetailView(DetailView):
    model = Course
    
    def get_object(self, queryset=None):
        code = self.kwargs['code']
        return get_object_or_404(Course, code=code)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        course = self.get_object()
        allowed_modules = course.allowed_modules.all()  # Access modules allowed for the course
        
        context['course'] = course
        context['allowed_modules'] = allowed_modules
        
        return context


class MyRegistrationsListView(ListView):
    model = Registration
    template_name = 'mrreporting/my_registrations.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Registration.objects.filter(user=user).order_by('module__name')
    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'mrreporting/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context.update({'title': 'Contact Us'})


        return context
    
    def contact(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']

                message = form.cleaned_data['message']
                EmailMessage(
                    'Contact Form Submission from {}'.format(name),
                    message,
                    'form-response@SIT.com',
                    ['c0033267@shu.ac.uk'],
                    [],
                    reply_to=[email]
                ).send() 
                messages.success(self.request, 'Successfully sent the enquiry')
                return super().form_valid(form)
            
            else:

                form = ContactForm()
                return render(request, 'mrreporting/contact.html', {'form': form}) 
            
    
   ## def form_valid(self, form):

      ###  messages.success(self.request, 'Successfully sent the enquiry')

      ###  form.send_mail()
       ### 
        ###return super().form_valid(form)
        
        


  ##  def form_invalid(self, form):
    ###    messages.warning(self.request, 'Unable to send the enquiry')
    ###    return super().form_invalid(form)
    
    def get_success_url(self):
          return self.request.path