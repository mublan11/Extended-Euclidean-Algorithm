# -*- coding: utf-8 -*-
"""
    Autores: Diego Misael Blanco Murillo, 
             Alexandro Ivan Garcia Perez,
             Cruz Eduardo Lopez
"""
def euclides(inverso, modulo):
    modulo0 = modulo
    x0, x1, y0, y1 = 1, 0, 0, 1
    while modulo != 0:
        q, inverso, modulo = inverso // modulo, modulo, inverso % modulo
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1    
    if x0 < 0:
        x0 += modulo0
    return x0

inverso = int(input('Inverso: '))
modulo = int(input('Modulo: '))
try:
    print ('Resultado:',euclides(inverso, modulo))
except Exception as e:
    print (e)
