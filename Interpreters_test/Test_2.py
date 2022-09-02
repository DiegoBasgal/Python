texto = "falou!  loucura vei. mto bruto seloko     dois leais:? sera que deu certo etc. dddescubra, aa."
entrada = list(texto)
frases = []
i = 0

while entrada != []:
    if i == len(entrada)-1:
        frases.append("")
        for a in range(0, i + 1):
            frases[len(frases) - 1] = frases[len(frases) - 1] + entrada[a]
        for b in range(0, i + 1):
            entrada.pop(0)
        i = 0
    elif entrada[i] == " " and i != 0 and i < len(entrada)-2 and i < len(entrada):
        if entrada[i+1] == " " and entrada[i+2] ==" " and entrada[i-1] != " ":
            frases.append("")
            for a in range(0, i+1):
                frases[len(frases)-1] = frases[len(frases)-1] + entrada[a]
            for b in range(0, i+1):
                entrada.pop(0)
            i = 0
        else:
            i = i + 1

    elif entrada[i] == "?" or entrada[i] == "!" or entrada[i] == ":?" or entrada[i] == "!" or entrada[i] == ":!":
        frases.append("")
        for a in range(0, i+1):
            frases[len(frases)-1] = frases[len(frases)-1] + entrada[a]
        for b in range(0, i+1):
            entrada.pop(0)
        i = 0

    elif entrada[i] == ".":
        if i > 3:
            if entrada[i-1] == "c" and entrada[i-2] == "t" and entrada[i-3] == "e" and entrada[i-4] == " ":
                i = i + 1
            else: 
                frases.append("")
                for a in range(0, i+1):
                    frases[len(frases)-1] = frases[len(frases)-1] + entrada[a]
                for b in range(0, i+1):
                    entrada.pop(0)
                i = 0
        else:
            frases.append("")
            for a in range(0, i+1):
                frases[len(frases)-1] = frases[len(frases)-1] + entrada[a]
            for b in range(0, i+1):
                entrada.pop(0)
            i = 0
    else:
        i = i + 1

print(frases)
