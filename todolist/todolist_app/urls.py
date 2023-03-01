from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name="todos"),
    path('todo/<str:pk>/', views.single_todo, name="single_todo"),
    path('create_todo/', views.create_todo, name="create_todo"),
    path('update_project/<str:>/', views.update_todo, name="update_project"),
]
