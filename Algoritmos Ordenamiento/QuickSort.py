def quicksort(Datos, inf, sup):
    i = inf
    j = sup
    x = Datos[(inf+sup)// 2]
    print('inf:', inf, '\nsup:', sup, '\ni:', i, '\nj', j, '\nX=', x)
    while (i < j):
        while (Datos[i] < x):
            print(Datos[i], '<', x)
            i = i + 1
            print('i:', i)

        while (Datos[j] > x):
            print(Datos[j], '>', x)
            j = j - 1
            print('j:', j)

        if (i <= j):
            aux = Datos[i]
            Datos[i] = Datos[j]
            Datos[j] = aux
            print('Aux=', aux, '\nA[', i, ']=', Datos[i], '\nA[', j, ']=', Datos[j])
            i = i + 1
            j = j - 1
        print('________________________________')
    if (inf < j):
        quicksort(Datos, inf, j)
    if (i < sup):
        quicksort(Datos, i, sup)
    
    return Datos

Datos = [10, 5, 2, 8] 
n = 3
quicksort(Datos, 0, n)