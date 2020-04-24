# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:51:23 2020

@author: Juan Rojas
"""


import numpy as np


def generador(min,max):
    arreglo = np.random.randint(min,max, size=48).reshape(4,12)
    return arreglo

def imprimir(array):
    ciudades = np.array(['B','F','G','P'])
    print('las dimensiones del arreglo son: ' +str(array.shape))
    print ('B=Bucaramanga','F=Floridablanca','G=Giron','P=Piedecuesta')
    print('','', 'Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic')
    
    for i in range(0,4):
        print(str(ciudades[i]) + str(array[i]))
        
ciudades = np.array(['B','F','G','P'])
mes = np.array(['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'])
        
ingresos = generador(100,181)
egresos = generador(60,131)

imprimir(ingresos)
imprimir(egresos)
        
def restador(arrayA,arrayB):
    arrayR= arrayA - arrayB
    return arrayR

ganancias = restador(ingresos,egresos)
imprimir(ganancias)

def mejor_ciudad(ganancias):
    filas, columnas = ganancias.shape
    v1 = 0
    v2 = 0 
    v3 = 0
    v4 = 0
    for mes in range(0,columnas):
        v1 += ganancias[0][mes]
        v2 += ganancias[1][mes]
        v3 += ganancias[2][mes]
        v4 += ganancias[3][mes]
    if v1>v2 and v1>v3 and v1>v4:
        mm = ('Bucaramanga')
    elif v2>v1 and v2>v3 and v2>v4:
        mm = ('Floridablanca')
    elif v3>v1 and v3>v2 and v3>v4:
        mm = ('Giron')
    elif v4>v1 and v3>v2 and v2>v3:
        mm = ('Piedecuesta')
    else:
        mm = ('hay 2 ciudades con las mismas ganancias')
    return mm

print(' la ciudad con mejores ganancias es' + ' ' + str(mejor_ciudad(ganancias)))

def peor_ciudad(ganancias):
    filas, columnas = ganancias.shape
    v1 = 0
    v2 = 0 
    v3 = 0
    v4 = 0
    for mes in range(0,columnas):
        v1 += ganancias[0][mes]
        v2 += ganancias[1][mes]
        v3 += ganancias[2][mes]
        v4 += ganancias[3][mes]
    if v1<v2 and v1<v3 and v1<v4:
        mm = ('bucaramanga')
    elif v2<v1 and v2<v3 and v2<v4:
        mm = ('Floridablanca')
    elif v3<v1 and v3<v2 and v3<v4:
        mm = ('Giron')
    elif v4<v1 and v3<v2 and v2<v3:
        mm = ('Piedecuesta')
    else:
        mm = ('hay 2 ciudades con las mismas perdidas')
    return mm

print(' la ciudad con peores ganancias es' + ' ' + str(peor_ciudad(ganancias)))

def mejor_mes(ganancias,mes,ciudades):
    
    for j in range(4):
        mayor = 0
        posicion = 0
        for i in range(12):
            if (ganancias[j][i] > mayor):
            
                posicion = i
                mayor = ganancias[j][i] 
        print('en la ciudad de',ciudades[j], 'el mejor mes fue', mes[posicion])
            
mejor_mes(ganancias,mes,ciudades)


def menor_mes(ganancias,mes,ciudades):

    for j in range(4):
        menor = ganancias[0][0]
        posicion = 0
        for i in range(12):
            if (ganancias[j][i] < menor): 
                posicion = i
                menor = ganancias[j][i] 
        print('en la ciudad de',ciudades[j], 'el menor mes fue', mes[posicion])
            
menor_mes(ganancias,mes,ciudades)


def imprimir_personalizado(arreglo,mesInicio,mesFin,nombre):
    for j in range(4):
        for i in range(12):
            if (i>=mesInicio and i<=mesFin):
                print('la ciudad',ciudades[j], nombre, mes[i],'fue',arreglo[j][i])
            
    
a=int(input('ingrese un mes de inicio: '))
b=int(input('ingrese un mes de fin: '))
c=int(input('ingrese 1 para elegir ganancias, 2 para ingresos o 3 para elegir egresos: '))
      
if c==2:
    imprimir_personalizado(ingresos,a-1,b-1,'ingresos')    
if c==1:
     imprimir_personalizado(ganancias,a-1,b-1,'ganancias')   
if c==3:
     imprimir_personalizado(egresos,a-1,b-1,'egresos')   
     
     
     
def promedio(array1,array2,array3):
    for j in range(4):
        acumIngresos = 0
        acumEgresos = 0
        acumGanancias = 0
        for i in range(12):
            acumIngresos += ingresos[j][i] 
            acumEgresos += egresos[j][i] 
            acumGanancias += ganancias[j][i] 
    
        print('en la ciudad',ciudades[j],'el promedio anual de ingresos fue: ',acumIngresos/12 ,'el promedio anual de egresos fue :',acumEgresos/12,'el promedio anual de ganancias fue :',acumGanancias/12)
        
            
promedio(ingresos,egresos,ganancias)

def promedio2(arreglo1,arreglo2,arreglo3):
    for j in range(4):
        acumIngresos = 0
        acumEgresos = 0
        acumGanancias = 0
        menor1 = arreglo1[0][0]
        menor2 = arreglo2[0][0]
        menor3 = arreglo3[0][0]
        mayor1 = 0
        mayor2 = 0
        mayor3 = 0
        for i in range(12):
            
            acumIngresos += arreglo1[j][i] 
            acumEgresos += arreglo2[j][i]
            acumGanancias += arreglo3[j][i]
            
            if (arreglo1[j][i] < menor1): 
                menor1 = arreglo1[j][i] 
                
            if (arreglo2[j][i] < menor2): 
                menor2 = arreglo2[j][i] 
                
            if (arreglo3[j][i] < menor3): 
                menor3 = arreglo3[j][i] 
            
            if (arreglo1[j][i] > mayor1):
                mayor1 = arreglo1[j][i] 
                
            if (arreglo2[j][i] > mayor2):
                mayor2 = arreglo2[j][i] 
                
            if (arreglo3[j][i] > mayor3):
                mayor3 = arreglo3[j][i] 
            
                 
        print('el promedio anual de la ciudad',ciudades[j],'en ingresos es: ',(acumIngresos-menor1-mayor1)/10, 'el promedio anual de egresos fue: ',(acumEgresos-menor2-mayor2)/10, 'el promedio anual de ganancias fue: ',(acumGanancias-menor3-mayor3)/10)

    
promedio2(ingresos,egresos,ganancias)
      
            
def extraer_proporciones(arreglo):
    for j in range(4):
        acumP = 0
        acumN = 0
        for i in range(12):
            if arreglo[j][i] < 0:
                acumN+= 1 
            if arreglo[j][i] > 0:
                acumP+=1
                
                
        print('el porcentaje de meses en ganancias de la ciudad: ',ciudades[j], 'es: ',acumP*8.33333,'%')
        print('el porcentaje de meses en perdidas de la ciudad: ',ciudades[j],'es: ',acumN*8.33333,'%')    
        
        
extraer_proporciones(ganancias)
            
                
    
            
            