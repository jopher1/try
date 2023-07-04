from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponse


def employee_index(request,id):
        return HttpResponse (f"<h1>Welcome <i style='color:red'>{id}</i></h1>")


# Create your views here.

def employee_list(request):
    
    return render(request, "reg_empuser/employee_list.html")

def employee_form(request):
    form = EmployeeForm()
    return render(request,"reg_empuser/employee_form.html",{'form':form})

def employee_delete (request):
    return 

