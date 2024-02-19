from TodoApp.views import MainForm, TodoView

from django.urls import path

urlpatterns=[
    path('', MainForm, name='MainForm'),

    path('MainForm', TodoView, name='TodoView')
]