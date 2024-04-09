# users/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='users_profile')
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    course = models.ForeignKey('mrreporting.Course', null=True, on_delete=models.SET_NULL, related_name='student')
    

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
