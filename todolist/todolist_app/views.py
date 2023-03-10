from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todos')
    context = {'form': form}
    return render(request, 'todolist_app/todo_form.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')

    context = {"form": form}
    return render(request, 'todolist_app/todo_form.html', context)


def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todos')
    context = {"object": todo}

    return render(request, 'todolist_app/delete_template.html', context)


