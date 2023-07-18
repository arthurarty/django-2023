from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from projects.models import Project


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world")


def project_list(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {
        'projects': projects
    })

def project_detail(request: HttpRequest, pk: int) -> HttpResponse:
    project = Project.objects.get(pk=pk)
    return render(
        request, 'projects/detail.html', {
            'project': project
        }
    )
