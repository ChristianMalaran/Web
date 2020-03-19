from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Todo

# Create your views here.
def todo_list(request):
    
    context = {'todo_list': Todo.objects.all()}

    return render(request, 'home.html', context)

def insert_list(request: HttpRequest):
    
    todo = Todo(content=request.POST['content'])
    todo.save()

    return redirect('/todos/list')

def delete_list(request, todo_id):

    delete = Todo.objects.get(id=todo_id)
    delete.delete()
    
    return redirect('/todos/list')




    
# def todo_list(request):
#     context = {'todo_list': Todo.objects.all()}
#     return render(request, 'home.html', context)

# def insert_list(request: HttpRequest):

#     todo = Todo(content = request.POST['content'])
#     todo.save()

#     return redirect('/todo/list')

# def delete_list(request, todo_id):
#     delete = Todo.objects.get(id=todo_id)
#     delete.delete()
#     return redirect('/todo/list')