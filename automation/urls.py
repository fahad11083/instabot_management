from django.urls import path

from . import views

app_name = 'automation'
urlpatterns = [
    path('create', views.create, name='create'),
]
