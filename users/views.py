from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
        
            user = form.save()
            
            profile = Profile.objects.get(users_profile=user)
            profile.course = form.cleaned_data['course']
            profile.save()


            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('mrreporting:login')

        else:
            messages.warning(request, 'Unable to create account!')
            return redirect('mrreporting:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form ,'title': 'Student Registration'})

@login_required
def profile(request):

    has_profile_profile = hasattr(request.user, 'profile')
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user) 
        p_form = ProfileUpdateForm(instance = request.user.profile) if has_profile_profile else None
        context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'} 
        return render(request, 'users/profile.html', context)
