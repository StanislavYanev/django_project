from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse('31 days')


def february(request):
    return HttpResponse('28 days')


def march(request):
    return HttpResponse('31 days')


def april(request):
    return HttpResponse('30 days')


def may(request):
    return HttpResponse('31 days')


def june(request):
    return HttpResponse('30 days')


def july(request):
    return HttpResponse('31 days')


def august(request):
    return HttpResponse('31 days')


def september(request):
    return HttpResponse('30 days')


def october(request):
    return HttpResponse('31 days')


def november(request):
    return HttpResponse('30 days')


def december(request):
    return HttpResponse('31 days')
# Create your views here.
