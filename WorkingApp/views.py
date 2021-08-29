from django.shortcuts import render
from django.http import HttpResponse

def LandingPage(request):
    return HttpResponse('You have landed successfully on the page of the Working App.')