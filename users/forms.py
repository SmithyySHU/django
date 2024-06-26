from django import forms
from dobwidget import DateOfBirthWidget
from django.contrib.auth.models import User
from .models import Profile
from mrreporting.models import Course, Registration


from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    date_of_birth = forms.DateField(label = 'Date Of Birth', widget=DateOfBirthWidget(),)
    address = forms.CharField(label = "Address", help_text= "Enter your address name and number")
    city_town = forms.CharField(label = "City/Town", help_text= "Enter your Town or City")
    country = forms.CharField(label = "Country", help_text= "Enter your country")
    course = forms.ModelChoiceField (queryset=Course.objects.all(), required=True, empty_label="Pick ya course")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','date_of_birth','address','city_town','country','course','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    address = forms.CharField()
    city_town = forms.CharField()
    country = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','date_of_birth','address','city_town','country']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



