from django.shortcuts import render
from .models import project
import numpy as np
import matplotlib.pyplot as plt
from random import randint


def index(request):
    object = project.objects.all()
    print(object)
    dict = {
        'title':'страница',
        'project':object
    }
    return render(request, 'lab/index.html',dict)

def webApp(request):
    return render(request, 'lab/webApp.html')

def chatBot(request):
    return render(request, 'lab/chatBot.html')

def ML(request):
    return render(request, 'lab/ML.html')

def Games(request):
    return render(request, 'lab/Games.html')

def tester(request):
    return render(request, 'lab/tester.html')

def casper(request):
    def factorial(n):
        m=1
        for i in range(1,n+1):
            m = m*i
        return m
    print(factorial(9))
    def random(n):
        sum=0
        for i in range(n):
            a=randint(1,11)
            sum+=a
            print(a,end='+')
        return sum
    print(random(10))

    def average(n):
        sum = 0
        for i in range(n):
            a = int(input())
            sum+=a
        return sum/n

    print(average(2))

    def newton(v0,g):
        time = 2*v0/g
        t = np.linspace(0,time,1000)
        h = v0*t - 0.5*g*t**2
        print(max(h))
        plt.figure(figsize=(4,3))
        plt.plot(t,h)
        plt.show()
    newton(30,10)
    return render(request, 'lab/casper.html')









