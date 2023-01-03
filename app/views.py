from pydoc import describe
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Todo
# Create your views here.
def home(request):
    a=Todo.objects.all()
    return render(request,'home.html',{'todo':a})

def add(request):
    if request.method == 'GET':
       return render(request,'add.html')

    else:
        t=request.POST['title']
        d=request.POST['description']
        Todo.objects.create(title=t,description=d)
        return redirect('home')

def delete(request,id):
    Todo.objects.get(id=id).delete()
    return redirect('home')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('home')

def mark_completed(request,id):
    todo=Todo.objects.get(id=id)
    todo.is_completed=not todo.is_completed
    todo.save()
    return redirect('home')

def edit(request,id):
    try:
       todo=Todo.objects.get(id=id)
       if request.method == 'GET':
          return render(request,'edit.html',{'todo':todo})
    
       else:
          t=request.POST['title']
          d=request.POST['description']
          todo.title=t
          todo.description=d
          todo.save()
          return redirect('home')

    except:
        return HttpResponse("Todo id doesnot exist.")