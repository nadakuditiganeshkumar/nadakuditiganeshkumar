from django.contrib import admin

# Register your models here.
from .models import Department,Employee

from .models import UserProfileInfo
# Department admin
admin.site.register(Department)

#Employee Admin
class EmpAdmin(admin.ModelAdmin):
    list_display = ['employee_name','dob','joining_date','manager','weight','salary','city']

admin.site.register(Employee,EmpAdmin)

#login

admin.site.register(UserProfileInfo)