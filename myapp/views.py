from django.http import HttpResponse
from django.http import JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return HttpResponse("<h1>About</h1>")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse('task: %s' % task.title)
