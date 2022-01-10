dato = 4
A = [9, 5, 4, 12, 2]
n = 4
enc = False
i = 0
while (i <= n and enc == False):
    if (dato == A[i]):
        print(A[i], '==', dato)
        enc = True
    else:
        print(A[i], '==', dato)
        i = i + 1

if (enc == True):
    print('El valor se ha encontrado')
else:
    print('El valor no se ha encontrado')