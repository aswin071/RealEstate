from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.add_property, name='add_property'),
    path('properties/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('properties/<int:pk>/delete/', views.delete_property, name='delete_property'),
    path('tenant/<int:tenant_id>/', views.tenant_profile, name='tenant_profile'),
    path('assign_tenant/', views.assign_tenant, name='assign_tenant'),
    path('search/', views.search, name='search'),
    
]
