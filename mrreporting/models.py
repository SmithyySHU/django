from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    level = models.FloatField()
    students = models.ManyToManyField(User, related_name='courses')

    def __str__(self):
        return self.name
    
class Module(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    credit = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    courses_allowed = models.ManyToManyField(Course, related_name='allowed_modules')

    def __str__(self):
        return self.name