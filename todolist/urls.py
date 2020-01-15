from django.urls import path
from todolist import views

urlpatterns = [
    path('',views.home),
    path('addTodo/',views.addTodo),
    path('delete/<int:todo_id>',views.delete),
    path('completed/<int:todo_id>',views.completed),
]
