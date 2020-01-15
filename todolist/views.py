from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def home(request):
	all_todo_items=TodoItem.objects.all()
	return render(request,'index.html',{"all_items":all_todo_items})

def addTodo(request):
	if request.POST['content']!='':
		new_item=TodoItem(content=request.POST['content'],completed=False)
		new_item.save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def delete(request,todo_id):
	delete_todo=TodoItem.objects.get(id=todo_id)
	delete_todo.delete()
	return HttpResponseRedirect('/')

def completed(request,todo_id):
	todo=TodoItem.objects.get(id=todo_id)
	todo.completed=True
	todo.save()
	return HttpResponseRedirect('/')