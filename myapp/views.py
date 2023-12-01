
#Se necesita para retornar una respuesta de Htt(Texto que va a recibir el navegador.)
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request,'index.html',{
        'title': title
    })

#Parametro "request" lo entrega python.
def hello(request, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    #task = Task.objects.get(title=title)
    return render(request, 'tasks.html')
