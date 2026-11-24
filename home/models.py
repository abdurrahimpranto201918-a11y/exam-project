from django.db import models

# Create your models here.
class Student(models.Model) :
    name = models.CharField(max_length=15, null=True, blank = True)
    email = models.EmailField(max_length=30, null=True, unique=True, blank = True)
    roll = models.PositiveIntegerField(null=True, unique=True, blank = True)
    registration = models.IntegerField(null=True, blank = True)
    image = models.ImageField(upload_to='stu_images/', height_field=None, width_field=None, max_length=None, null=True, blank=True, default='stu_images/default.png')
    
    
class Teacher(models.Model) :
    name = models.CharField(max_length=15, null=True, blank = True)
    email = models.EmailField(max_length=254, null=True, unique=True, blank = True)
    image = models.ImageField(upload_to='tch_images/', max_length=None, null=True, blank=True, default='teacher_images/default.png')
