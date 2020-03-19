from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/lists')

def lists(request):

    x = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_list.html', x)

def delete(request,id):
    
    delete = Employee.objects.get(pk=id)
    delete.delete()

    return redirect('/employee/lists')