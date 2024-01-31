from django.urls import path
from users import views as user_views


from . import views

app_name = 'mrreporting'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('modules', views.modules, name = 'modules'),
    path('register', user_views.register, name = 'register'),
]