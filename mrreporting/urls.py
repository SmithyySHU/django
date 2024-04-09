from django.urls import path
from users import views as user_views
from mrreporting import views as mrreporting_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'mrreporting'

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('modules', views.module, name = 'modules'),
    path('register', user_views.register, name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile', user_views.profile, name = 'profile'),
    path('course', views.course, name = 'course'),
    path('module/<str:code>/', mrreporting_views.ModuleDetailView.as_view(), name = 'module'),
    path('module/<int:pk>/register/', mrreporting_views.register_for_module, name='register_for_module'),            
    path('remove-registration/<int:pk>/', mrreporting_views.remove_registration, name='remove_registration'),       

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)