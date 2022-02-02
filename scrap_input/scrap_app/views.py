from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse(render(request, 'home.html'))


def login_page(request):
    return HttpResponse(render(request, 'login.html'))


def input_page(request):
    return HttpResponse(render(request, 'input.html'))


def overview_page(request):
    return HttpResponse(render(request, 'overview.html'))
