# -*- coding: utf-8 -*-

Codice per la risoluzione di sistemi lineare (Work in progress)
"""
Created on Thu Dec 13 21:15:56 2018

@author: Riccardo Coriani

@description: jacobi method for solving linear systems 'Au = b'
"""

import numpy as np
from numpy import linalg


# Reading data from csv file corresponding to the A matrix

data1 = np.genfromtxt("matrice.csv", delimiter=';')
data = np.array(data1)
del data1
print(np.linalg.det(data))    #Da fare dopo, se det=0 non andare avanti

x = data[:,0]
dim = len(x)     # per sapere la dimensione del sistema
del x
# Building a diagonal matrix (diag) and an Upper U and a lower L triangular matrices

diag = np.matrix.diagonal(data)
L = np.tril(data, -1)
U = np.triu(data, 1)
# Going on allocating the solution's vector u
#sol_old = np.random.rand(dim)

#sol_old = np.zeros(dim, dtype=float)
sol_old = np.array([1,1,1])
sol_u = np.zeros(dim, dtype=float)

# write the term b form console
b = [-1, 4, 2 ]

sums = 0
a =np.array(dim, dtype = float)
a = (1/diag)

it = 0
while it < 20:
    i = 0
    while i < dim:
        j = 0
        while j < dim:
            sums = sums + L[i,j]*sol_old[j] + U[i,j]*sol_old[j]
            j = j + 1
        sol_u[i] =a[i]*(b[i] - sums)
        sums = 0
        i = i + 1    
    sol_old = sol_u
    it = it + 1
#sol_old = sol_u
    
print(sol_u)