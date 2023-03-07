from django.shortcuts import render
from .forms import Studentregistration
from .models import Student
from django.http.response import HttpResponseRedirect
# Create your views here.

def showdata(request):
    fm=Studentregistration()
    table=Student.objects.all()
    return render(request,'index.html',{'data':fm,'table':table})

def add(request):
    fm=Studentregistration(request.POST)
    if fm.is_valid():
        name=fm.cleaned_data['name']
        section=fm.cleaned_data['section']
        contact=fm.cleaned_data['contact']
        email=fm.cleaned_data['email']
        school=fm.cleaned_data['school']
        reg=Student(name=name,section=section,contact=contact,email=email,school=school)
        reg.save()
        fm=Studentregistration()
        table=Student.objects.all()
        msg={'data save sucessfully'}
        return render(request,'index.html',{'data':fm,'msg':msg,'table':table})


def delete(request,id):
    res=Student.objects.get(pk=id)
    res.delete()
    return HttpResponseRedirect('/')
