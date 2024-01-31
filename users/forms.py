from django import forms
from dobwidget import DateOfBirthWidget
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')
    date_of_birth = forms.DateField(label = 'Date Of Birth', widget=DateOfBirthWidget(),)
    address = forms.CharField(label = "Address", help_text= "Enter your address name and number")
    city_town = forms.CharField(label = "City/Town", help_text= "Enter your Town or City")
    country = forms.CharField(label = "Country", help_text= "Enter your country")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','date_of_birth','address','city_town','country','password1', 'password2']