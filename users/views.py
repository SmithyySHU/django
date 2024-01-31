from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
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
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'}



    return render(request, 'users/profile.html', context)

