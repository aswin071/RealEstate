from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.add_property, name='add_property'),
    path('properties/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('properties/<int:pk>/delete/', views.delete_property, name='delete_property'),
    
]
