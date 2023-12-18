from django import forms
from .models import TaskModel
from category import models

class addTask(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields ="__all__"



    
