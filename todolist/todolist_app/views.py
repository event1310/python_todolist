from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def todos(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, 'todolist_app/todos.html', context)


def single_todo(request, pk):
    todoObj = Todo.objects.get(id=pk)
    return render(request, 'todolist_app/single-todo.html', {"todo": todoObj})


def create_todo(request):
    form = TodoForm()
    context = {'form': form}
    return render(request, 'todolist_app/todo_form.html', context)


