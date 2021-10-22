"""pages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from layout import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('adduser/',views.adduser,name='adduser'),
    path('list/',views.list,name='list'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('dele_conf/<int:id>', views.dele_conf, name='dele_conf'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
    path('logout/', views.log_out, name='logout'),
    path('qf/<str:employee_name>', views.quaryf, name='qf'),
    path('fil', views.filtr, name='fil'),
    path('exc',views.excul,name='exc'),

]
