Datos = [7, 5, 2, 11]
n = 3
i = 0
cambiado = True
while (i < n and cambiado == True):
    j = n
    cambiado = False
    print('_________________________________________________________')
    print('Cambiado: ', cambiado)
    while (j > i):
        print('n:', n, '\ni:', i)
        print('j:', j)
        if (Datos[j] < Datos[j-1]):
            cambiado = True
            Aux = Datos [j]
            Datos [j] = Datos [j-1]
            Datos [j-1] = Aux
            print('Cambiado:', cambiado, '\nAux:', Aux)
            print(Datos[j], '>', Datos[j-1])
            print('A[', j , ']=', Datos[j])
            print('A[', j - 1, ']=', Aux)
            print('----------------')
        
        j = j - 1

    i = i + 1