from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task
import json

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return redirect("task_list")

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        data = json.loads(request.body)
        new_title = data.get("title", "").strip()
        if new_title:
            task.title = new_title
            task.save()
            return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completed = True
        task.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})