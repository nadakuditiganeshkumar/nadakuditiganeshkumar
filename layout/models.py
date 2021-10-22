import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
#DEPARTMENT MODEL
class Department(models.Model):
    department_name=models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

#EMPLOYEE MODEL
class Employee(models.Model):
    employee_name=models.CharField(max_length=250)
    dob=models.DateField()
    joining_date=models.DateField()
    manager=models.CharField(max_length=250)
    weight=models.IntegerField()
    salary=models.BigIntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    city=models.CharField(max_length=250)

    def __str__(self):
        return self.employee_name


#USER LOGIN MODELS

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Add any addtional attributes you want
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username



