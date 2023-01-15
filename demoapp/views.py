from django.shortcuts import render,HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pm = form.cleaned_data['password']
            reg = User(name = nm, email=em, password=pm ) # to reg. name and email
            reg.save()
            form = UserForm() 
    else:
        form = UserForm()
    std = User.objects.all()
    return render(request,'addshow.html',{'form':form,'userinfo':std})


def update_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = UserForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
    return render(request,'update.html',{'form':fm})
    

def delete_data(request,id):
    if request.method == "POST":
        us = User.objects.get(pk = id)
        us.delete()
    return HttpResponseRedirect('/')