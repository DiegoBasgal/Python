import re
regex = r"[a-zA-z0-9][a-zA-z0-9]*[@][a-zA-z0-9]*[.]([a-zA-z0-9]*[.][a-zA-z0-9]*|[a-zA-z0-9]*)"
test_str = ("PUCPR/PPGIA\n"
            "Bloco 8 - Parque Tecnológico - 2o andar\n"
            "Rua Imaculada Conceição, 1155 - Prado Velho\n"
            "CEP 80215-901 - Curitiba - PR\n"
            "27281-421\n"
            "cel: (024)99846-4403\n"
            "data: 04/10/2019\n"
            "email: bragawilliams@yahoo.com.br\n")
'''
Telefone =  r"[(][0][0-9]{2}[)][0-9]{5}[-][0-9]{4}"

Data = r"(([0-2][0-9])|([3][0|1]))[\/]([0][1-9]|[1][0-2])[\/]([0-1][0-9]{3}|[2][0][0-1][0-9])"

Email = r"[a-zA-z0-9][a-zA-z0-9]*[@][a-zA-z0-9]*[.]([a-zA-z0-9]*[.][a-zA-z0-9]*|[a-zA-z0-9]*)"

Cep = r"[0-9]{5}[-]([0-9]{3}[ ]|[0-9]{3}\s)"

'''


matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    print("Match (matchNum) encontrado em {start}-{end}: {match}".format(matchNum = matchNum,
                                                                          start = match.start(),
                                                                          end = match.end(),
                                                                          match = match.group()))
