from django.shortcuts import render
import sys, os

# Create your views here.

def home(request):
    return render(request, '_home.html', {'title':'title'})


def script(request):
    x = []
    y = []
    if request.method == 'POST':
        x = request.POST.get('x_field')
        y = request.POST.get('y_field')
        for data in x:
            print(x)
    return None