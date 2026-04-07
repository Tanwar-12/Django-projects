from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import EmployeeForm
from myapp.models import Employee

def home(request):
    return render(request, "home.html")

def createEmp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")
    else:
        form = EmployeeForm()
    return render(request, "index.html", {"form": form})

def show(request):
    emp = Employee.objects.all()
    return render(request, "show.html", {"emp": emp})

def edit_employee(request, eid):
    emp = get_object_or_404(Employee, eid=eid)
    return render(request, "edit.html", {"empl": emp})

def update_employee(request, eid):
    emp = get_object_or_404(Employee, eid=eid)
    if request.method == "POST":
        emp.ename = request.POST.get("ename")
        emp.email = request.POST.get("email")
        emp.phone = request.POST.get("phone")
        emp.save()
        return redirect("show")
    return render(request, "edit.html", {"empl": emp})

def delete_employee(request, eid):
    emp = get_object_or_404(Employee, eid=eid)
    emp.delete()
    return redirect("show")