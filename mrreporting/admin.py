from django.contrib import admin
from .models import Module
from .models import Course
# Register your models here.
admin.site.register(Module)
admin.site.register(Course)