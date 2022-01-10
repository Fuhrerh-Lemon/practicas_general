dato = 6
A = [7, 13, 6, 10, 8]
n = 4
enc= False
pos = 0
while (pos < n and enc == False):
    print('Pos:', pos)
    print(A[pos], '==', dato)
    if (A[pos] == dato):
        enc = True
    else:
        pos = pos + 1

if (enc == True):
    print('El valor se ha encontrado')
else:
    print('El valor no se ha encontrado')