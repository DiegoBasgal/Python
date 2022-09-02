import re 

regex = r"[a-z]"
test_str = ("PUCPR/PPGIA\n"
            "Bloco 8 – Parque Tecnológico – 2o andar\n"
            "Rua Imaculada Conceição, 1155 - Prado Velho\n"
            "CEP 80215-901 - Curitiba – PR")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    print ("matchNum {matchNum} encontrado em {start}-{end}: {match}".format(matchNum = matchNum,
                                                                             start = match.start(),
                                                                             end = match.end(),
                                                                             match = match.group()))