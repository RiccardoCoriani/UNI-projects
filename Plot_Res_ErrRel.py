# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:37:38 2018

@author: Riccardo Coriani
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def nans(shape, dtype=float):
    a = np.empty(shape, dtype)
    a.fill(np.nan)
    return a

# Reading Direct data from txt file. 
data = np.loadtxt("Dati_Ordinati_D_48.txt", skiprows = 1)
data1 = np.loadtxt("Dati_Ordinati_I_48.txt", skiprows = 1)
# Creation of vectors R_d standing for the Resistance of the direct method
Rd = data[:,4]
dimD = len(Rd)
Ri = data1[:,4]
dimI = len(Ri)
# Creation of the Coordinate's matrix
CoorD = np.delete(data,4,1)
CoorI = np.delete(data1,4,1)


# Now the cycle for the Relative Error. The variable c counts the number of
# equal coordinates

c = 0
while 1:
    if np.array_equal(CoorD[c,:] , CoorI[c,:]) == True:
      c += 1
    else:
        break

dim = dimD + dimI - c

Ri_Tot = nans(dim)
C_Tot =nans([dim,4])

# Definition of Rd_Tot
Rd_Tot = Rd
Rd_Tot = np.append(Rd_Tot, nans(dimI-c)) 

# Cycles for Ri_Tot
i = 0
while i < c:
    Ri_Tot[i] = Ri[i]
    i += 1
i = dimD
while i < dim:
    Ri_Tot[i] = Ri[i-dimD+c]
    i += 1

# Cycles for C_Tot
i = 0
while i < dimD:
    C_Tot[i,:] = CoorD[i,:]
    i += 1
j = c
while j < dimI:
    C_Tot[i,:] = CoorI[j,:]
    i += 1
    j += 1
    
 # Definition of the relative error   
Err = np.empty(c)     #  Relative Error Array
i = 0
while i < c:
    if np.array_equal(CoorD[i,:] , CoorI[i,:]) == True:
       Err[i] = abs((Ri[i]-Rd[i])/(Rd[i] + Ri[i]))
       i += 1
    else:
        break

Err_Tot = nans(dim)
i = 0
while i < c:
    Err_Tot[i] = Err[i]
    i += 1

# Definition of the final data set
#np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})


Final_Dataset= np.zeros([dim,7])
j = 0
while j < 4:
    Final_Dataset[:,j] = np.trunc(C_Tot[:,j])
    j += 1
Final_Dataset[:,j] = np.round(Rd_Tot,5)
Final_Dataset[:,j+1] = np.round(Ri_Tot,5)
Final_Dataset[:,j+2] = np.round(Err_Tot,5)

print(C_Tot)
''' Saving part of the code  '''

#with open('Pippo&Pluto.dat', 'w') as out_file:
#    title = 'A(M)        B(N)        M(A)       N(B)      Rd       Ri   ErrRel \n'
#    out_file.write(title)
#    for i in range(len(Rd_Tot)):     # Change also here if you are changing the file
#        out_string = ''
#        out_string += str(Final_Dataset[i,:]) + '\n'   # And here
#        out_file.write(out_string)
#        print(out_string)










#### Disttribution of the relaative error
#
#mpl.pyplot.figure('Histo_Err')
#mpl.pyplot.hist(Err*100, 25, (0,100), histtype = 'stepfilled')
#mpl.pyplot.title('Distribuzione delle frequenze errore percentuale (48 el)')
#mpl.pyplot.xlabel('valore in % ')
#mpl.pyplot.ylabel('Frequenza')
#mpl.pyplot.savefig('Frequeze_Errore_Relativo-48.jpg')


##%%
#from mpl_toolkits.mplot3d import Axes3D
#
#
#
## Building the coordinates
#A = data[:,0]
#B = data[:,1]
#M = data[:,2]
#N = data[:,3]
#
#A1 = data1[:,0]
#B1 = data1[:,1]
#M1 = data1[:,2]
#N1 = data1[:,3]
#
#a_ab = abs(B - A)
#a_mn = abs(N - M)
#
#a_ab1 = abs(B1 - A1)
#a_mn1 = abs(N1 - M1)
#
#n = abs(M - B)
#n1 = abs(A1 - N1)
#  
#C = (a_ab + a_mn + 2*n)/4
#C1 = (a_ab1 + a_mn1 + 2*n1)/4
#
#h = C
#Cg = ((A + B)/2) + C
#
#h1 = C1
#Cg1 = ((M1 + N1)/2) + C1    # Already the centre to be used in the canvas
#
## The 3D coordinates are:  Cg as x  ;  h as y  ;  R for z
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
##ax.scatter3D(Cg, h, abs(Rd), s=50, c='blue', depthshade=True)
#
#ax.bar3d(Cg, h, abs(Rd), 1,1,0.5, shade= True)
##ax.bar3d(Cg1, h1, abs(Ri), 1,1,0.5, color = 'r', shade= True)
#
#ax.set_xlabel('Numero Elettrodo')
#ax.set_ylabel('Profondità')
#ax.set_zlabel('Resistività')
#plt.grid(True)
#plt.show()
##plt.savefig('Histo3D.pdf')
#
#
