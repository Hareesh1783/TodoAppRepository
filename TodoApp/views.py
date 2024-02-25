from django.shortcuts import render, redirect

from TodoApp.models import TodoTable

# Create your views here.

def MainForm(request):
    return render(request, 'Home.html')

def TodoView(request):
<<<<<<< HEAD
    List=TodoTable.objects.all()
    context={'ListOfTodos': List}
    return render(request, 'TodoList.html', context)
=======
    return render(request, 'TodoList.html')
>>>>>>> refs/remotes/origin/master
