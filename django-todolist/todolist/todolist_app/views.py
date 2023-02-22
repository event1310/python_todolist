from django.shortcuts import render
from django.http import HttpResponse

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
    site = "todos"
    selectednumber = 25
    favnumber = 25

    context = {"currensite": site, "favnumber": favnumber, "selectednumber": selectednumber, "todos": todosList}

    return render(request, 'todolist_app/todos.html', context)


def single_todo(request, pk):
    todoObj = None
    for i in todosList:
        if i['id'] == pk:
            todoObj = i
    return render(request, 'todolist_app/single-todo.html', {"todoObjs": todoObj})
















