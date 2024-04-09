from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    level = models.FloatField()
    students = models.ManyToManyField('auth.User', related_name='courses')
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=Course)
def update_user_courses(sender, instance, **kwargs):
    """
    Signal handler to update the user's courses when a Course is saved.
    """
    students = instance.students.all()
    if students.count() > 1:
        # If a student is assigned to more than one course, remove them from other courses
        for student in students.exclude(pk=instance.students.first().pk):
            student.courses.clear()
    
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
