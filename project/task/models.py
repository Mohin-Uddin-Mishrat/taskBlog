from django.db import models
from category.models import categoryModel

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateField()  
    category = models.ManyToManyField(categoryModel )
    
    def __str__(self) :
        return f"{self.taskTitle}"
