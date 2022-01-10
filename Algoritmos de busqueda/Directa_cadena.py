p = ['A', 'D', 'E']
t = ['C', 'A', 'D', 'E', 'N', 'A']
m = len(p) 
n = len(t) 
i = 0
j = 0
while (i < n and j < m):
    print('i:', i, '\nj:', j)
    if (t[i] == p[j]):
        print(t[i], '==', p[j])
        i = i + 1
        j = j + 1
    else:
        print(t[i], '==', p[j])
        i = i - j + 1
        j = 0

if (j == m):
    print('El valor se ha encontrado')
else:
    print('El valor no se ha encontrado')