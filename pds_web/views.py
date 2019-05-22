import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from matplotlib.animation import PillowWriter
from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline
from collections import defaultdict


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
    



def zplane(z, p, filename=None):
    
    ax = plt.subplot(2, 2, 1)
    
    # Adicionando circulo e eixos zero
    unit_circle = patches.Circle((0,0), radius=1, fill=False,
                                 color='black', ls='solid', alpha=0.1)
    ax.add_patch(unit_circle)
    axvline(0, color='0.7')
    axhline(0, color='0.7')
 
    # Plotando os polos e setando propiedades
    poles = plt.plot(p.real, p.imag, 'x', markersize=9, alpha=0.5)

    
    # Plotando os zeros e setando propiedades
    zeros = plt.plot(z.real, z.imag,  'o', markersize=9, 
             color='none', alpha=0.5,
             markeredgecolor=poles[0].get_color(),
             )

     
    # Escala para ajustar
    r = 1.5 * np.amax(np.concatenate((abs(z), abs(p), [1])))
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])

    
    """
    Caso existam multiplos polos ou zeros no mesmo ponto
    """
    # Procurando corrdenadas duplicados no mesmo pixel
    poles_xy = ax.transData.transform(np.vstack(poles[0].get_data()).T)
    zeros_xy = ax.transData.transform(np.vstack(zeros[0].get_data()).T)    

    # dict deve ser inteiro e coords deve ser float

    # TODO reduzindo duplicações
    d = defaultdict(int)
    coords = defaultdict(tuple)
    for xy in poles_xy:
        key = tuple(np.rint(xy).astype('int'))
        d[key] += 1
        coords[key] = xy
    for key, value in d.items():
        if value > 1:
            x, y = ax.transData.inverted().transform(coords[key])
            plt.text(x, y, 
                        r' ${}^{' + str(value) + '}$',
                        fontsize=13,
                        )

    d = defaultdict(int)
    coords = defaultdict(tuple)
    for xy in zeros_xy:
        key = tuple(np.rint(xy).astype('int'))
        d[key] += 1
        coords[key] = xy
    for key, value in d.items():
        if value > 1:
            x, y = ax.transData.inverted().transform(coords[key])
            plt.text(x, y, 
                        r' ${}^{' + str(value) + '}$',
                        fontsize=13,
                        )

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
        print ('Plote dos Polos e zero salvos em ' + str(filename))



    # b = list(map(int, input().split()))
    # a = list(map(int, input().split()))

    # b = array(b) # ENTRAR COM O POLINÔMIO DE ENTRADA AQUI ==-------<==========-------<==========-------<==========-------<====
    # a = array(a)

    # # Descobrindo os polos e zeros
    # z, p, k = tf2zpk(b, a)

    # # Plotando os zeros e polos
    # figure(figsize=(16, 9))
    # subplot(2, 2, 1)
    # zplane(z, p)
    # grid(True, color='0.9', linestyle='-', which='both', axis='both')
    # title('Poles and zeros')

    # # Printando os zeros e polos
    # print (str(len(z)) + " zeros: " + str(z))
    # print (str(len(p)) + " poles: " + str(p))



@csrf_exempt
def z_transform_request(request):
    from scipy.signal import (freqz, butter, bessel, cheby1, cheby2, ellip, 
                            tf2zpk, zpk2tf, lfilter, buttap, bilinear, cheb2ord, cheb2ap
                            )
    from numpy import asarray, tan, array, pi, arange, cos, log10, unwrap, angle
    from matplotlib.pyplot import (stem, title, grid, show, plot, xlabel, 
                                ylabel, subplot, xscale, figure, xlim, 
                                margins)
    a = []
    b = []
    if request.method == "POST":
        b = request.POST.get('den_signal').split()
        a = request.POST.get('num_signal').split()
        print(a, b)
        
        #transformando de str para float
        a = [float(i) for i in a]
        b = [float(n) for n in b]


        b = array(b) # ENTRAR COM O POLINÔMIO DE ENTRADA AQUI ==-------<==========-------<==========-------<==========-------<====
        a = array(a)


        z, p, k = tf2zpk(b, a)
        print("aqui")

        z = z.tolist()
        p = p.tolist()


        z = [float(i) for i in z]
        p = [float(n) for n in p]


        return JsonResponse({'success': 'true', 'zeros': z, 'poles': p})
    else:
        return JsonResponse({'success': 'false'})