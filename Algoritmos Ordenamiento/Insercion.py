Datos = [7, 13, 6, 10, 8]
n = len(Datos)
i = 0
while (i < n):
    j= i
    Aux = Datos[i]
    print('_________________________________________________________')
    print('n:', n, '\ni:', i, '\nj:', j)
    print('Aux:',Aux)
    while (j > 0 and Aux < Datos[j-1]):
        Datos[j] = Datos[j-1]
        print('Cambio::', Aux, '<', Datos[j-1])
        print('A[', j , ']=', Datos[j])
        j = j - 1
    
    Datos[j] = Aux
    i = i + 1
    print('Cambio hecho:::', Datos)