# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:30:42 2020

@author: Juan Rojas
"""

ss = {"colombia":[4.7, 5.7, 5.1],
      "Peru":[4.6, 4.4, 3.4, 5.7, 3.1],
      "Ecuador":[4.6, 4.4, 3.4, 5.7, 3.1],
      "Chile":[4.6, 5.1, 6.0, 4.1, 4.4],
      "Argentina":[3.6, 4.8, 5.1, 4.5],
      "Brasil":[4.1, 4.4, 3.7]
      }
#¿Cual es el numero de sismos que han ocurrido en cada pais en le transcurso del 2020
print("la cantidad de sismos ocurridos en cada pais es:")
cantidad_sismos = {}
for pais in ss:
    cantidad_sismos[pais] = len(ss[pais])
    print(pais,cantidad_sismos[pais])
    
print("")    
    
#¿En que paises han ocurrido 4 o mas sismos?
print("los paises que tienen 4 o mas sismos")
mayor_sismos = {}
for pais in ss:
       if len(ss[pais])  >= 4:
        print(pais,ss[pais])
        
print("")

#¿Cual es el promedio de sismos en cada pais
print("promedio en cada pais es:")
prom_sismos_cada_pais= {}
for pais in ss:
    prom_sismos_cada_pais[pais] = round(
        sum(ss[pais])/len(ss[pais]),2)
    print(pais,prom_sismos_cada_pais[pais])
    



    
