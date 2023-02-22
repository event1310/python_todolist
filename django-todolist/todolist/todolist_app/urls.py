from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name="todos"),
    path('todo/<str:pk>/', views.single_todo, name="single_todo"),
]