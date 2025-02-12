from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Add_task_form
from .models import Task,Status


def home_view(request):
    list_tasks = Task.objects.all()
    return render(request,'index.html',{"tasks":list_tasks})

def add_task_view(request):
    if request.method == "POST":
        form = Add_task_form(request.POST)
        
        if form:
            title = form["title"].value()
            description = form["description"].value()
            new_task = Task.objects.create(title=title,description=description)
            if new_task:
                print(new_task)
                new_task.save()
                return redirect("home")
            
            else:
                redirect("new_task")
            
        
    return render(request,"new_task.html",{"form":Add_task_form})

def edit_task(request,id:int):
    task_obj = Task.objects.get(id=id)
    status_obj = Status.objects.all()
    
    if request.method == "POST":
        new_title = request.POST.get('title') or None
        new_description = request.POST.get('description') or None
        new_status = request.POST.get('status','')
        new_status_int = int(new_status)
        new_status = Status.objects.get(id=new_status_int)
        print(f"New data:\nTitle:{new_title}\nDescription:{new_description}\nStatus:{new_status}")
        
        if new_title:
            task_obj.title = new_title
            task_obj.save()
        if new_description:
            task_obj.description = new_description
            task_obj.save()
        if new_status:
            task_obj.status = new_status
            task_obj.save()
        else:
            print("Error: Unable to update task data")
            
        return redirect("home")
                        
    else:
        return render(request,'edit_task.html',{'task':task_obj,"Status":status_obj})
    
def remove_task(request,id):
    task_obj = Task.objects.get(id=id)
    task_obj.delete()
    return redirect("home")