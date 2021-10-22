from django import forms

from .models import Employee,Department
from django.contrib.auth.models import User
from .models import UserProfileInfo
# from django.contrib.auth.forms import UserCreationForm


class Empform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class Depform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


#USER FORMS

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

