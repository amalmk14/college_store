from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField()
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    address = models.TextField(max_length=500)
    materials = models.TextField(max_length=200)
    purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name







# from django.db import models
#
# # Create your models here.
# class Task(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     age = models.IntegerField(max_length=2)
#     gender = models.CharField(max_length=10)
#     phone = models.IntegerField(max_length=10)
#     email = models.EmailField()
#     address = models.TextField(max_length=100)
#     department = models.CharField(max_length=100)
#     course = models.CharField(max_length=100)
#     priority = models.TextField(max_length=100)
#     materials = models.TextField(max_length=100)
#
#     def __str__(self):
#         return self.name
