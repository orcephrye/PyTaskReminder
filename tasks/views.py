from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Tasks


def index(request):
    current_tasks = list(filter(lambda x: x.is_valid, Tasks.objects.order_by("-time_from")))
    return render(request, "tasks/index.html", {"current_tasks": current_tasks})


def history(request):
    history_tasks = list(filter(lambda x: not x.is_valid, Tasks.objects.order_by("-time_from")))
    return render(request, "tasks/history.html", {"history_tasks": history_tasks})


def new_task(request):
    return HttpResponse("You are posting a task")


def detail(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task, "isValid": task.is_valid()})


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("polls:index"))
