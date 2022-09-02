
from collections import Counter
from nltk import tokenize
import nltk
import stanfordnlp
from nltk.corpus import stopwords


#Case folding (texto para minúsculo) +
#tokenizacao +
#Forma Canônica
#stemming +
#Lematização (versão 2) +
#Remoção de stopwords +

texto = input("Coloque seu texto")


def tokenizacao(texto):
    print('\n\nContar tokens cm o NLTK: ')

    palavras_tokenize = tokenize.word_tokenize(texto.casefold(),language='portuguese')

    print(palavras_tokenize)
    contador = Counter(palavras_tokenize)

    for cont in contador.items():
        print(cont)

def lematizacao(var):
    parsec_text = {'word':[],'lemma':[]}
    for sent in doc.sentences:
        for wrd in sent.words:
            parsec_text['word'].append(wrd.text)
            parsec_text['lemma'].append((wrd.lemma))
        return parsec_text


nlp = stanfordnlp.Pipeline(lang='pt')
doc = nlp(texto)
print(lematizacao(doc))


def stopword():
    print('\n\n', set(stopwords.words('portuguese')))

tokenizacao(texto)
lematizacao(texto)
stopword()

