def heapify(Datos, m, j):
    max = j
    leftChild = 2 * j + 1
    rightChild = 2 * j + 2
    print(m, j, '---------')
    print('Max: ', max, '\nleft: ', leftChild, '\nright: ', rightChild)

    if (leftChild < m and Datos[leftChild] > Datos[max]):
        print(leftChild, '<', m, '   Y   ', Datos[leftChild], '>', Datos[max])
        max = leftChild
        print('Max: ', max)

    if (rightChild < m and Datos[rightChild] > Datos[max]):
        print(rightChild, '<', m, '   Y   ', Datos[rightChild], '>', Datos[max])
        max = rightChild
        print('Max: ', max)

    if (max != j):
        swap = Datos[j]
        Datos[j] = Datos[max]
        print('Swap: ', swap)
        Datos[max] = swap
        print('A[', i, '] = ', Datos[j], '\nA[', max, '] = ', Datos[max])
        heapify(Datos, m, max)
        print('_________________________________')
        
    return Datos

Datos = [12, 8, 3, 5]
n = 4
i = n//2 - 1
k = n - 1

while (i >= 0):
    heapify(Datos, n, i)
    i = i - 1

while (k >= 0):
    print('K:', k)
    tmp = Datos[0]
    Datos[0] = Datos[k]
    Datos[k] = tmp
    print('tmp:', tmp)
    print('A[0]:', Datos[0])
    heapify(Datos, k, 0)
    k = k - 1