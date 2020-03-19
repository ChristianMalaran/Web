from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todo_list, name="todo_list"),
    path('insert/', views.insert_list, name="insert_list"),
    path('delete/<int:todo_id>', views.delete_list, name="delete_list"),

]
