from django.http import HttpResponse
from django.shortcuts import render


def buttons(request):
    return HttpResponse("hi!")

