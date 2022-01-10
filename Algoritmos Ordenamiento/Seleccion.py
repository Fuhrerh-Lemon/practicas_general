Datos = [9,5,4,12,2]
n = len(Datos)
i = 0
while (i < n):
    mindice = i
    j = i + 1
    print('_________________________________________________________')
    print('n:', n, '\ni:', i + 1)
    print('indice:', mindice + 1, '\nj', j + 1)
    while (j < n):
        if (Datos[j] < Datos[mindice]):
            mindice = j
            print('cambio::', Datos[i], '>', Datos[mindice])
            print('Indice:', mindice)
        j = j + 1
    Aux = Datos[i]
    Datos[i] = Datos[mindice]
    Datos[mindice] = Aux
    print('Aux:', Aux)
    print('A[', i  , ']=', Datos[i])
    print('A[', j , ']=', Aux)
    i = i + 1
    print('Cambio hecho:::', Datos)