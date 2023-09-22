from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('employee/',views.employeeApi),
    path('employee/<int:id>',views.employeeApi),   
    path('employee/leave/',views.leaveApi),
    path('employee/leave/<int:id>',views.leaveApi),   
    path('app_admin/',views.app_adminApi),

]
