
# Pesquisa Sequencial 
def ex1(x, V, n):
    i = 0                           # C1
    k = -1                          # C2
    while (i < n) and (k == -1):    # C3
        if x == V[ i ]:             # C4
            k = i                   # C5
        else:                       # C6
            if V[ i ] < x:          # C7
                i = i + 1           # C8
            else:                   # C9
                k = -2              # C10
    return k                        # C11

X = [1,2,3,23,43,45,50,100]
print(ex1(101, X, len(X)))

# Ordenação por Bolha 
def ex2(V, n):
    nt = 0 # número de trocas       #C1
    while True:                     #C2
        nt= 0                       #C3
        for k in range(0, n-1, 1):  #C4
            if (V[k] > V[k+1]):     #C5
                aux = V[k]          #C6
                V[k] = V[k+1]       #C7
                V[k+1] = aux        #C8
                nt = nt + 1         #C9
        if nt == 0:                 #C10
            break                   #C11

X = [9,8,7,6,5,4,3]
ex2(X, len(X))
print(X)

# Ordenação por Bolha Modificada 
def ex3(V, n):
    fim = n - 1                     #C1
    while True:                     #C2
        kk = 0;                     #C3
        for k in range(0, fim, 1):  #C4
            if V[k] > V[k + 1]:     #C5
                aux = V[k]          #C6
                V[k] = V[k + 1]     #C7
                V[k + 1] = aux      #C8
                kk = k              #C9
        fim = kk                    #C10
        if kk == 0:                 #C11
            break                   #C12

X = [9,8,7,6,5,4,3]

ex3(X, len(X))
print(X)

# Busca do Valor Máximo de um Vetor 
def ex4(V, n):
    max = V[ 0 ]                #C1
    for i in range(1, n, 1):    #C2
        if V[i] > max:          #C3
            max = V[i]          #C4
    return max                  #C5

X = [9,8,7,6,5,4,3,50]

a = ex4(X, len(X))
print(a)

# Busca do Valor MinMax de um Vetor 
def ex5(V, n):
    min = V[0]                          #C1
    max = V[0]                          #C2
    for i in range(1, n, 1):            #C3
        if V[i] < min:                  #C4
            min = V[i]                  #C5
        if V[i] > max:                  #C6
            max = V[i]                  #C7
    return [['max', max],['min', min]]  #C8


X = [9,8,7,6,5,4,3,50]

a = ex5(X, len(X))
print(a)

# Busca do Valor MinMax melhorado de um Vetor 
def ex6(V, n):
    min = V[0]                          #C1
    max = V[0]                          #C2
    k = 0
    for i in range(1, n, 1):            #C3
        if V[i] < min:                  #C4
            min = V[i]                  #C5
        elif V[i] > max:                #C6
            max = V[i]                  #C7
    return [['max', max],['min', min]]  #C8


X = [10,9,8,7,6,5,4,3,2,1]
#X = [1,2,3,4,5,6,7,8,9,10]

a = ex6(X, len(X))
print(a)

# ordenação por inserção
def ex7(V, n):
    for j in range(1, n, 1):            #C1
        chave = V[ j ]                  #C2
        i = j - 1                       #C3
        while i >= 0 and V[i] > chave:  #C4
            V[i + 1] = V[ i ]           #C5
            i = i - 1                   #C6
        V[i + 1] = chave                #C7
    return V

X = [6,5,4,3,2,1]
#X = [1,2,3,4,5,6]
#X = [5,2,4,6,1,3]
print(ex7(X, len(X)))
