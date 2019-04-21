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
    print(request)
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

@csrf_exempt
def convolution_request(request):
    input_signal = []
    kernel = []
    if request.method == "POST":
        input_signal = request.POST.get('input_signal').split(',')
        kernel = request.POST.get('kernel').split(',')

        #transformando de str para float
        input_signal = [int(i) for i in input_signal]
        kernel = [int(n) for n in kernel]

        input_time = list(range(len(input_signal)))
        kernel_time = list(range(len(kernel)))

        d = process_convolution(input_signal, input_time, kernel, kernel_time)

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

def convolution(y1, y2):
    res = []
    print(y1)
    print(y2)
    outPutLengh = len(y1) + len(y2) - 1
    for i in range(outPutLengh):
        kmin = i - (len(y2) - 1) if(i >= len(y2) - 1) else 0
        kmax = i if(i < len(y1) - 1) else len(y1) - 1

        sum = 0
        for k in range(kmin, kmax+1):
            sum += y2[i-k]*y1[k]
        res.append(sum)
    return res

def process_convolution(input_signal, input_time, kernel_signal, kernel_time):
    """
    Eixo do tempo do sinal Convolucionado
    """
    convolution_x_axis = list(range(input_time[0] + kernel_time[0], len(input_signal) + len(kernel_signal) - 1))
    convolution_y_axis = convolution(kernel_signal, input_signal)
    print(convolution_x_axis, convolution_y_axis)

    res = []

    for a, b in zip(convolution_x_axis, convolution_y_axis):
        res.append({'x': a, 'y': b})
    print(res)
    return res
    
