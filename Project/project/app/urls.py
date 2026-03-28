# app - urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('debug/', views.debug_photos),
    path('', views.user_list, name='user-list'),
    path('Add/', views.AddUser, name='add-user'),
    path('Edit/<int:id>/', views.EditUser, name='edit-user'),
    path('Delete/<int:eid>/', views.DeleteUser, name='delete-user'),
    path('View/<int:eid>/', views.ViewUser, name='view-user'),
    
]