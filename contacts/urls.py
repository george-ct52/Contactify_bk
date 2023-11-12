from turtle import update
from django.urls import path
from .views import create_contact, get_contacts, delete_contact,update_contact

urlpatterns = [
    path('contacts/', get_contacts, name='get_contacts'),
    path('contacts/create/', create_contact, name='create_contact'),
    path('contacts/delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('contacts/edit_contact/<int:pk>/', update_contact, name='update_contact'),
]