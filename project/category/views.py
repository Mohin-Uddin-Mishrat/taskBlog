from django.shortcuts import render
from . import forms
def category(req):

    if req.method == 'POST':
        form= forms.addcategory(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return render(req, 'cat.html', {"form":form})
    else:
        form= forms.addcategory()
        return render(req, 'cat.html', {"form":form})
 
 