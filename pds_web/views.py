import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from matplotlib.animation import PillowWriter
from matplotlib import rc

# Create your views here.

def home(request):
    return render(request, '_home.html', {'title':'title'})

@csrf_exempt
def script(request):
    x = []
    y = []
    if request.method == "POST":
        for data in x:
            print(data)
        x = request.POST.get('x_field').split(',')
        y = request.POST.get('y_field').split(',')
        representacao_sinal(x,y)

        return JsonResponse({'success': 'ok'})
    else:
        return JsonResponse({'success': 'false'})

def representacao_sinal(x, y):
    """
    Plot do Sinal
    """
    x = [float(i) for i in x]
    y = [float(n) for n in y]

    print(x)
    print(y)
    plt.title("Input Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    # help(plt.stem)
    plt.stem(x,y)
    plt.savefig("templates/pics/repres.png", dpi=400)
    #plt.grid()

