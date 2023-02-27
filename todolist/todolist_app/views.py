from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

todosList = [
    {
        'id': '1',
        'title': 'go to school',
        'date': '22.02.2023',
        'description': 'Go to school and educate myself'
    },
    {
        'id': '2',
        'title': 'buy tomatoes',
        'date': '23.02.2023',
        'description': 'Tomatoes approx 0.5kg'
    },
    {
        'id': '3',
        'title': 'run for 10 minutes',
        'date': '24.02.2023',
        'description': 'go for a quick run!'
    },
]


def todos(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, 'todolist_app/todos.html', context)


def single_todo(request, pk):
    todoObj = Todo.objects.get(id=pk)
    return render(request, 'todolist_app/single-todo.html', {"todo": todoObj})
















