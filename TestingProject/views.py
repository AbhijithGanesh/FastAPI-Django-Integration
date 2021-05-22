from django.shortcuts import render

def On_Landing(request):
    return render(request, 'App/index.html')