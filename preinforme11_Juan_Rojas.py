# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:59:19 2020

@author: Juan Rojas
"""


import numpy as np

def numeros():
    cantidad = np.array([[56,12,86,15,12],
                         [13,98,78,56,12],
                         [78,23,46,21,81]])
    
    return cantidad

def Orden(cantidad):
    
    Ordenanza = np.sort(cantidad)[::-1]
    return Ordenanza

def Largo():
    len(cantidad)

cantidad = numeros()

def Shape():
  cantidad.shape
