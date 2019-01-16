import random
import matplotlib
import pylab
import numpy


#Diofanto
'''
x = numpy.linspace(-75,75,1000) # 1000 linearly spaced numbers
y = (x**3) -80*(x**2) +1700*x - 10000
lista = []
lista_aprox = [0.01]

temp = 0
for _ in range(1000000):
    z = random.randint(-75,75)
    fz = z**3 -80*z**2 +1700*z - 10000
    fz_squared = fz**2
    lista_aprox.append(fz_squared)
    if lista_aprox[1] < lista_aprox[2]:
        lista_aprox.pop()
    if fz == 0:
        temp = z
        lista.append(temp)
        if lista.count(temp) == 1:
            print(f' A raiz é: {temp}')


pylab.plot(x,y) 
pylab.show()

'''
'''
x = numpy.linspace(-75,75,1000) # 1000 linearly spaced numbers
y = (x**3) -80*(x**2) +1700*x - 10000
lista = []
lista_aprox = [0.01]

temp = 0
temp_2 = 0
for _ in range(1000):
    z = random.uniform(-75,75)
    fz = z**3 -80*z**2 +1700*z - 10000
    fz_squared = fz**2
    lista_aprox.append(fz_squared)
    if lista_aprox[-2] < lista_aprox[-1]:
        lista_aprox.pop()
        temp_2 = z
        print(lista_aprox)
        #print(f'({temp_2},{fz_squared})')


pylab.plot(x,y) 
pylab.show()

'''

lista_aprox = [10]
temp = 0

for _ in range(100000):
    z = random.uniform(5,60)
    fz = z**3 -80*(z**2) +1700*z - 10000
    if (fz**2) < min(lista_aprox): 
        lista_aprox.append(fz**2)
        temp = z
print(min(lista_aprox))
print(temp)
print(lista_aprox)
#input()
