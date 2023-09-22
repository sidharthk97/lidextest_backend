
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from leave_app.models import Employee, Leave
from leave_app.serializers import EmployeeSerializer, LeaveSerializer



# Create your views here.

@csrf_exempt
def employeeApi(request,id=0):

    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    

    elif request.method == 'POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee Details Added Successfully",safe=False)
        else:
            employee_exists = Employee.objects.filter(user_id = employee_data["user_id"]).exists()
            if employee_exists :
                return JsonResponse("Employee userID already exists..... Not unique!",safe=False)
            # exist fn not checked in if part because user_id in model was created as unique=True
            else :
                pass

            return JsonResponse("Failed to Add Employee",safe=False)
    

    elif request.method == 'PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(id=id)
        employee_serializer=EmployeeSerializer(employee, data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee details Updated Successfully",safe=False)
        
        return JsonResponse("Failed to Update")
    

    elif request.method == 'DELETE':
        employee=Employee.objects.get(id=id)
        employee.delete()

        return JsonResponse("Employee Deleted Successfully",safe=False)
    


@csrf_exempt
def leaveApi(request,id=0):

    if request.method=='GET':
        leave = Leave.objects.all()
        leave_serializer=LeaveSerializer(leave,many=True)
        return JsonResponse(leave_serializer.data,safe=False)
    

    elif request.method=='POST':
        leave_data=JSONParser().parse(request) 
        leave_data.update({"status":"Pending"})  
        # all leave request created must have pending status until status changed by admin
        leave_serializer=LeaveSerializer(data = leave_data) 
        if leave_serializer.is_valid():
            leave_serializer.save()
            return JsonResponse("Leave application created Successfully",safe=False)
        
        return JsonResponse("Failed to create leave application",safe=False)
    

    elif request.method=='PUT':
        leave_data=JSONParser().parse(request)
        leave=Leave.objects.get(id=id)
        leave_serializer=LeaveSerializer(leave, data = leave_data)
        if leave_serializer.is_valid():
            leave_serializer.save()
            return JsonResponse("leave details Modified Successfully",safe=False)
        
        return JsonResponse("Failed to Modify leave application")
    

    elif request.method=='DELETE':
        leave = Leave.objects.get(id=id)
        leave.delete()

        return JsonResponse("Leave application Deleted Successfully",safe=False)
    

@csrf_exempt
def app_adminApi(request):
    pass
