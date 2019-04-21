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

        #transformando de str para float
        x = [int(i) for i in x]
        y = [int(n) for n in y]

        d = representacao_sinal(x,y)

        return JsonResponse({'success': 'true', 'signal': d})
    else:
        return JsonResponse({'success': 'false'})

def representacao_sinal(x, y):
    """
    Plot do Sinal
    """
    res = []

    for a, b in zip(x, y):
        res.append({'x': a, 'y': b})
    print(res)
    return res
    # plt.title("Input Signal")
    # plt.xlabel("Time")
    # plt.ylabel("Amplitude")
    # help(plt.stem)
    # plt.stem(x,y)
    # plt.savefig("static/pics/repres.png", dpi=400)
    #plt.grid()

