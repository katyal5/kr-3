import math
import os
clear = lambda: os.system('cls')
clear()
def crivolin1(x1,x2):
    s1=(x2*x2*x2*x2/4-2*x2*x2*x2/3+x2*x2)-(x1*x1*x1*x1/4-2*x1*x1*x1/3+x1*x1)
    return(s1)
def f(x):
    f=2*x*x*x-2*x*x+2*x-10
    return(f)
def simpson(f, x1, x2, n):
    h=(x2-x1)/n
    k=0.0
    x=x1 + h
    m=int(n/2+1)
    for i in range(1,m):
        k += 4*f(x)
        x += 2*h
    for i in range(1,m-1):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(x1)+f(x2)+k)
def conv():
 x1,x2=map(int,input("введите координаты x1 и x2:").split())
 n=int(input('введите шаг для оценки погрешности:'))
 s1=crivolin1(x1,x2)
 s2=simpson(f, x1, x2, n)
 print('площадь без погрешности равна ',s1)
 print('площадь с погрешностью равна ',s2)
 print("вам нужна оценка погрешности?(1-да,0-нет)")
 choice = input('введите свой выбор:\n')
 choice = int(choice)
 if choice is 1: print(abs(s1-s2))
 print('вы хотите использовать программу ещё раз?(1/0)')
 p=int(input())
 if p==1:
    clear()
    conv()
 else:
    clear()
    print('спасибо воспользовались этой программой')
    input()
conv()
