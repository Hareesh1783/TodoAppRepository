from django.shortcuts import render, redirect

# Create your views here.

def MainForm(request):
    return render(request, 'Home.html')

def TodoView(request):
    return render(request, 'TodoList.html')
