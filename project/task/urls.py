
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add ,name = 'add' ),
    path('', views.show ,name = 'show' ),
    path('delete/<int:id>', views.delete ,name = 'delete' ),
    path('edit/<int:id>', views.edit ,name = 'edit' ),
]
