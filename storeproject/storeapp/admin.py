from django.contrib import admin
from .models import Task,Department,Course,Purpose

# Register your models here.
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Purpose)

