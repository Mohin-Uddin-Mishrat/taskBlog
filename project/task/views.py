from django.shortcuts import render, redirect
from .models import TaskModel
from . import forms
def add(req):

    if req.method == 'POST':
        form= forms.addTask(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form= forms.addTask()
            return render(req, 'cat.html', {"form":form})
        
        return render(req, 'cat.html', {"form":form})
    form= forms.addTask()
    return render(req, 'cat.html', {"form":form})
 
 

def show(req):
    data = TaskModel.objects.all()

    return render(req , 'show.html',{"data":data})

def delete(req , id):
    data = TaskModel.objects.get(id = id).delete()

    return redirect('show')
     
def edit(req , id):
    data = TaskModel.objects.get(id = id)
    form = forms.addTask(instance = data)
    if req.method == "POST":
         form = forms.addTask(req.POST, instance = data)
         if form.is_valid():
             form.save()
             return redirect('show')     
    return render(req, 'add.html', {"form":form})
     
