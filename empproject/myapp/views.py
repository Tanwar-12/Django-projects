from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee


#Save Data
def createEmp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Saved")
            return redirect("/show")
        else:
            return render(request,"index.html",{"form":form})
    else:
        form=EmployeeForm()
    return render(request,"index.html",{"form":form})
# Create your views here.

def show(request):
    emp=Employee.objects.all()#select * from employee
    return render(request,"show.html",{"emp":emp})

def edit(request,eid):
    empl=Employee.objects.get(eid=eid)
    return render(request,'edit.html',{"empl":empl})

def update(request,eid):
    empl=Employee.objects.get(eid=eid)
    print(eid)
    form=EmployeeForm(request.POST,instance=empl)
    if form.is_valid():
        form.save()
        return redirect("/show")
    
    return render(request,"edit.html",{"empl":empl})

def delete(request,eid):
    empl=Employee.objects.get(eid=eid)
    empl.delete()
    return redirect("/show")