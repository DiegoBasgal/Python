"""
    n-gram
    Para o cálculo da similaridade, usar a fórmula:
        S=2C/A+B
        Sendo:
            A é o número de n-gramas únicos na primeira palavra
            B é o número de n-gramas únicos na segunda palavra
            C é o número de digramas únicos compartilhados
            S=2*2/2+5=0.58
"""

def gram(word):
    di=[]

    for i in range(len(word)-1):
        a = word[i] + word[i + 1]
        if a in di:
            di.remove(a)
        else:
            di.append(a)
    return di

def sim(di1, di2):
    c = 0

    for i in di1:
        for j in di2:
            if i == j:
                c = c + 1

    return 2*c / (len(di1) + len(di2))

def sugerir(word):
    a = {}

    for i in lex:
        a.__setitem__(i, sim(gram(word), gram(i)))

# Create a list of tuples sorted by index 1 i.e. value field
    listofTuples = sorted(a.items(), reverse=True, key=lambda x: x[1])
# Iterate over the sorted sequence
    for elem in listofTuples:
        if elem != word and elem[1] > 0.1:
            print(elem[0], "::", elem[1])

lex = ["abacate", "abacaxi", "abobora", "abobrinha", "ananas", "maça", "mamao", "manga",
                        "melancia", "melao", "mexerica", "morango"]

sugerir("abacati")












