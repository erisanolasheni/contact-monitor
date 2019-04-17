# url urls
from django.urls import path
from .views import indexHome, indexContacts, createContacts

urlpatterns = [
    path('', indexHome, name='home'),
    path('contacts', indexContacts, name='contacts'),
    path('create', createContacts, name='create')
]