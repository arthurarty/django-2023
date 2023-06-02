from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world")


def project_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects/index.html')
