from django.urls import path
from .views import landing
app_name='deskapp'
urlpatterns=[path('',landing, name='landing')]