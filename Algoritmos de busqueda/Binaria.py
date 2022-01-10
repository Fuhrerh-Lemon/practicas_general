dato = 23
A = [4, 10, 12, 27]
n = 4
inf = 0
sup = n 
enc = False
while (inf <= sup and enc == False):
    print('inf', inf, 'sup', sup)
    centro = (sup + inf) // 2
    print('centro:', centro)
    if (A[centro] == dato):
        enc = True
    else:
        if (dato < A[centro]):
            sup = centro - 1
        else:
            inf = centro + 1
    print(A[centro], '==', dato)

if (enc == True):
    print('El valor se ha encontrado')
else:
    print('El valor no se ha encontrado')

