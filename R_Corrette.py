# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:29:14 2019

Programma di correzione dei valori delle resistenze. Dove si hanno due misure
diverse di resistenza, queste verranno pesate in base al valore delle resistenze
vicine. Come peso viene usata la discrepanza tra queste misure diverse e la
misura che viene considerata buona.
Se l'errore relativo tra le misure diverse è piccolo (sotto una certa soglia),
non verrà applicato questo peso ma verrà presa la media semplice tra le misure 
"""

import numpy as np

data = np.loadtxt("DatiStimaR48.dat", skiprows = 1)


C = data[:,4]
h = data[:,5] 
Rd = data[:,6]
Ri = data[:,7]


# Il metodo per capire se abbiamo dei nan è fare la differenza tra i numeri 
# in una stessa posizione: se è zro abbiamo dei numeri, se è nan abbiamo dei nan
# infatti nan - nan  = nan

# Creo il vettore delle resistenze stimate e comincio a riempirlo con i valori 
# che non hanno una coppia
R = np.zeros(len(Rd))

i = 0
v = []    # posizione delle coppie
while i < len(Rd):
    if (Rd[i] - Rd[i]) != 0 or (Ri[i] - Ri[i]) != 0:
        if (Rd[i] - Rd[i]) == 0:
            R[i] = Rd[i]
            i += 1
        else:
            R[i] = Ri[i]
            i += 1
    else:
        v = v + [i]
        i += 1

# I valori che hanno una coppia ma con errore relativo basso (sotto una
# certa soglia) li inserisco in R semplicemente facendone la media 
   
     
d = 0.3    #  SOGLIA ERRORE RELATIVO


i = 0
contatore = 0
vec = []   # vuovo vettore posizione delle coppie rimaste
while i < len(v):
    if abs((Rd[v[i]] - Ri[v[i]])/(Rd[v[i]] + Ri[v[i]])) <= d:
        R[v[i]] = (Rd[v[i]] + Ri[v[i]])/2
        contatore += 1
        i += 1
    else:
        vec = vec + [v[i]]
        i += 1

print('Numero di coppie trovate: ' + str(len(v)))
print('Numero di coppie trovate dentro la soglia: ' + str(contatore) )



# Ora si va a creare il ciclio per pesare le misure rimanenti seguendo la 
# discrepanza delle misure con il valore vicino a destra

c = 0
while c < 5:
    i = 0
    contatore = 0
    while i < len(vec):
        if h[vec[i]] == h[vec[i] + 1] and R[vec[i] + 1] != 0:
            p1 = abs((Rd[vec[i]] - R[vec[i] + 1]))/(Rd[vec[i]] + Ri[vec[i]])
            p2 = abs((Ri[vec[i]] - R[vec[i] + 1]))/(Rd[vec[i]] + Ri[vec[i]])
            Rstima = abs(p2/(p1+p2))*Rd[vec[i]] + abs(p1/(p1+p2))*Ri[vec[i]]
            R[vec[i]] = Rstima
            contatore += 1
            i += 1
        elif h[vec[i]-1] == h[vec[i]] and R[vec[i] - 1] != 0:
            p1 = abs((Rd[vec[i]] - R[vec[i] - 1]))/(Rd[vec[i]] + Ri[vec[i]])
            p2 = abs((Ri[vec[i]] - R[vec[i] - 1]))/(Rd[vec[i]] + Ri[vec[i]])
            Rstima = abs(p2/(p1+p2))*Rd[vec[i]] + abs(p1/(p1+p2))*Ri[vec[i]]
            R[vec[i]] = Rstima
            contatore += 1
            i += 1
        else:
            i += 1
    c += 1        

print('Coppie messe a posto con la discrepanza: ' + str(contatore))

np.set_printoptions(suppress=True)

DataSet = np.zeros([len(Rd), 5])
DataSet[:,0] = C
DataSet[:,1] = h
DataSet[:,2] = Rd
DataSet[:,3] = Ri
DataSet[:,4] = R

#with open('Pippo&Pluto.dat', 'w') as out_file:
#    title = 'Posizione    Profondità   R (d)    R (i)     Rstima\n'
#    out_file.write(title)
#    for i in range(len(Rd)):     # Change also here if you are changing the file
#        out_string = ''
#        out_string += str(DataSet[i,:]) + '\n'   # And here
#        out_file.write(out_string)
#        print(out_string)