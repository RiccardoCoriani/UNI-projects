# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:03:54 2018

@author: Riccardo Coriani
"""

import numpy as np
import matplotlib.pyplot as plt



# Reading Direct data from txt file. 
data = np.loadtxt("11-dd1-48-179_D.dat", skiprows = 9,
                  usecols = (1,3,5,7,9))

data1 = np.loadtxt("11-dd1-48-179_I.dat", skiprows = 9,
                  usecols = (1,3,5,7,9))
# Creation of the Coordinate's Vectors
A = data[:,0]
B = data[:,1]
M = data[:,2]
N = data[:,3]

A1 = data1[:,0]
B1 = data1[:,1]
M1 = data1[:,2]
N1 = data1[:,3]
# Creation of vectors R_d standing for the Resistance of the direct method
R_d = data[:,4]
R_i = data1[:,4]

# For example, to have the first set of coordinates of the quadrupole (AB-MN) 
# you have to write     CoorD[0,:] 
# I'm going now to define some useful quantities
 
dim = len(R_d)
dim1 = len(R_i)

# The distance a. The data show two different a, one for aAB and one for aMN

a_ab = abs(B - A)
a_mn = abs(N - M)

a_ab1 = abs(B1 - A1)
a_mn1 = abs(N1 - M1)
 
# The proportional factor n, now seen as the distance between B and M (so n = na)
    
n = abs(M - B)

n1 = abs(A1 - N1)

## The centre O of  A  B    .    M  N    

C = (a_ab + a_mn + 2*n)/4

C1 = (a_ab1 + a_mn1 + 2*n1)/4


## The deep factor h and the centre of the graphic Cg

h = C
Cg = ((A + B)/2) + C


h1 = C1
Cg1 = ((M1 + N1)/2) + C1

## Average distance
#j = 0
#ad = np.zeros(dim)
#
#while j < dim:
#    ad[j] = math.sqrt(abs(    A[j] - C[j]    ) * abs( B[j] -  C[j]  )   ) 
#    j += 1    



## Defining now the plot canvas

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.xaxis.tick_top()
plt.plot(Cg,-h, 'x', color = 'b', label = 'Diretta')
plt.plot(Cg1, -h1,'.', color = 'r', label = 'Inversa')  # multiplotting
plt.axis([0,96, -35,0])
plt.legend()
ax.xaxis.tick_top()


plt.xlabel('Numerazione elettrodi')
plt.ylabel('n')
plt.title('Posizione dei dati di resistività acquisiti con 96 elettrodi')

'''  plt.savefig('Figure_48')     '''
plt.show()



## log
#plt.subplot(222)
#plt.plot(x, y)
#plt.yscale('log')
#plt.title('log')
#plt.grid(True)