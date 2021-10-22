from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .forms import Empform, UserProfileInfoForm, UserForm
from .models import Employee,Department


# Main
def main(request):
    return render(request,'Main.html')

def log_out(request):
    return render(request,'logout.html')


def adduser(request):
    Emp = Empform()
    if request.method == 'POST':
        emp = Empform(request.POST, request.FILES)
        if emp.is_valid():
            emp.save()
        return redirect('list')
    return render(request,"base.html", {'form': Emp})


# list HTML
def list(request):
    emp=Employee.objects.all()
    dep=Department.objects.all()
    return render(request,'list.html',{'emp':emp,'dep':dep})

#FILTERS
#GET FUN
def quaryf(request,employee_name):
    emp=Employee.objects.get(employee_name='sai')
    return render(request,'qf.html',{'emp':emp})
#FILTER FUN
def filtr(request):
    emp=Employee.objects.filter(salary=25000)
    return render(request,'fil.html',{'emp':emp})

#EXCLUDE FUN

def excul(request):
    emp=Employee.objects.exclude(salary=25000)
    return render(request,'exc.html',{'emp':emp})

#EDIT FUNCTION
def edit(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        employee_name= request.POST['employee_name']
        joining_date= request.POST['joining_date']
        dob1 = request.POST['birth']
        manager= request.POST['manager']
        salary= request.POST['salary']
        city= request.POST['city']
        res_up = Employee.objects.get(id=id)
        res_up.employee_name = employee_name
        res_up.dob =dob1
        res_up.joining_date =joining_date
        res_up.manager = manager
        res_up.salary = salary
        res_up.city = city
        res_up.save()
        return redirect('list')
    return render(request,'edit.html',{'emp':emp})

#DELETE VIEWS

def delete(request,id):
    return render(request, 'delete.html',{'id': id})
def dele_conf(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('list')


#Login and Logout Views

@login_required()
def special(request):
    return HttpResponse("You are logged in, Nice! ")


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout'))


# Register view

def register(request):

    registered = False

    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm
        profile_form=UserProfileInfoForm
    return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form,
                                                   'registered':registered})


def user_login(request):

    if request.method =="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('list'))

            else:
                return HttpResponse("Account Not Active")
        else:
            return HttpResponse("Invalid Login Details Suppiled! UserName:{} and PassWord {}".format(username,password))
    #         return HttpResponse("UserName:{} and PassWord {}".format(username,password))
    #         return HttpResponse("Invalid Login Details Suppiled! ")
    else:
        # Nothing has been provided for username or password.
        return render(request,'login.html',{})
