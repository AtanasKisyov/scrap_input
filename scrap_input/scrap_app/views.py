from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('Home page coming soon...')


def login_page(request):
    return HttpResponse('Login page coming soon...')


def input_page(request):
    return HttpResponse(render(request, 'input.html'))


def scan_page(request):
    return HttpResponse('Scan page coming soon...')


def overview_page(request):
    return HttpResponse('Overview page coming soon...')
