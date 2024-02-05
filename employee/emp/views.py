from django.shortcuts import render
from emp.models import Employee
from emp.forms import Employeeform
def add(request):
    if(request.method=='POST'):
        form=Employeeform(request.POST)
        if(form.is_valid()):
            form.save()
            return view(request)
    form=Employeeform()
    return render(request,template_name='add.html',context={'form':form})

def view(request):
    b=Employee.objects.all
    return render(request,template_name='view.html',context={'b':b})

def edit(request,p):
    b=Employee.objects.get(id=p)
    if(request.method == 'POST'):
        form = Employeeform(request.POST,instance=b)
        if(form.is_valid()):
            form.save()
            return view(request)
    form = Employeeform(instance=b)
    return render(request, template_name='add.html', context={'form': form})

def delete(request,p):
    b=Employee.objects.get(id=p)
    b.delete()
    return view(request)