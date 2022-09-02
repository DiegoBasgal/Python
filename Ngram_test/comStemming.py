
from collections import Counter
from nltk import tokenize
import nltk
import stanfordnlp
from nltk.corpus import stopwords

texto = input("Coloque seu texto")

def tokenizacao(texto):
    print('\n\nContar tokens cm o NLTK: ')

    palavras_tokenize = tokenize.word_tokenize(texto.casefold(),language='portuguese')

    print(palavras_tokenize)
    contador = Counter(palavras_tokenize)

    for cont in contador.items():
        print(cont)


def stemming(texto):
    stemmer = nltk.stem.RSLPStemmer()
    print(stemmer.stem(texto))

def stopword():
    print('\n\n', set(stopwords.words('portuguese')))


tokenizacao(texto)
stemming(texto)
stopword()

