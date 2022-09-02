import stanfordnlp
from pycorenlp import StanfordCoreNLP

# The code below for part-of-speech was adapted from:
#      https://www.analyticsvidhya.com/blog/2019/02/stanfordnlp-nlp-library-python/

#dictionary that contains pos tags and their explanations
pos_dict = {
'CC': 'coordinating conjunction','CD': 'cardinal digit','DT': 'determiner',
'EX': 'existential there (like: \"there is\" ... think of it like \"there exists\")',
'FW': 'foreign word','IN':  'preposition/subordinating conjunction','JJ': 'adjective \'big\'',
'JJR': 'adjective, comparative \'bigger\'','JJS': 'adjective, superlative \'biggest\'',
'LS': 'list marker 1)','MD': 'modal could, will','NN': 'noun, singular \'desk\'',
'NNS': 'noun plural \'desks\'','NNP': 'proper noun, singular \'Harrison\'',
'NNPS': 'proper noun, plural \'Americans\'','PDT': 'predeterminer \'all the kids\'',
'POS': 'possessive ending parent\'s','PRP': 'personal pronoun I, he, she',
'PRP$': 'possessive pronoun my, his, hers','RB': 'adverb very, silently,',
'RBR': 'adverb, comparative better','RBS': 'adverb, superlative best',
'RP': 'particle give up','TO': 'to go \'to\' the store.','UH': 'interjection errrrrrrrm',
'VB': 'verb, base form take','VBD': 'verb, past tense took',
'VBG': 'verb, gerund/present participle taking','VBN': 'verb, past participle taken',
'VBP': 'verb, sing. present, non-3d take','VBZ': 'verb, 3rd person sing. present takes',
'WDT': 'wh-determiner which','WP': 'wh-pronoun who, what','WP$': 'possessive wh-pronoun whose',
'WRB': 'wh-abverb where, when','QF' : 'quantifier, bahut, thoda, kam (Hindi)','VM' : 'main verb',
'PSP' : 'postposition, common in indian langs','DEM' : 'demonstrative, common in indian langs'
}

for x in pos_dict:
  print('%s : %s' % (x, pos_dict[x]))

#extract parts of speech
def extract_pos(doc):
    parsed_text = {'word':[], 'POS':[], 'expl':[]}
    for sent in doc.sentences:
        for wrd in sent.words:
            if wrd.pos in pos_dict.keys():
                pos_exp = pos_dict[wrd.pos]
            else:
                pos_exp = 'NA'
            parsed_text['word'].append(wrd.text)
            parsed_text['POS'].append(wrd.pos)
            parsed_text['expl'].append(pos_exp)
    return parsed_text

# This sets up a default neural pipeline
'''
MODELS_DIR = '.'
stanfordnlp.download('en', MODELS_DIR)'''
nlp = stanfordnlp.Pipeline()
doc = nlp("Anna went to the supermarkets.")
result_pos = extract_pos(doc)

print('\n')
print('================= POS Tagging =================')
print('Sentence: "', doc.text,'"\n')

for type in result_pos:
  print('\nType: %s' % type)
  print('[')
  for item in result_pos[type]:
    print(item)
  print(']')

print('==================================')
print('\n')



print('=============== Dependency Parser ===================')
entrada = input("Digite a frase: ")
doc = nlp(entrada)

print('Sentence: "', doc.text,'"\n')

# Determine the syntatic head of each word in a
# sentence and the dependency relation between the
# two words that are accessible through word's governor
# and dependency_relation attributes
doc.sentences[0].print_dependencies()

# Capture the words of the sentence 
all_word_Structure = doc.sentences[0].words

# Show all the elements of the words
print('\n\nall_word_Structure:\n', all_word_Structure)
print('\n')


# Imprime manualmente cada elemento das tuplas das relacoes
for x in doc.sentences[0].words:
    print('(word: %s, relacao_com: %s, tipo_relacao: %s)' % (x.text, x.index, x.dependency_relation))
    print(x.dependency_relation)
print("\nPares verbosubstantivo:\n")
for i in range(len(doc.sentences[0].words)):
    print(doc.sentences[0].dependencies[i][2].text,doc.sentences[0].dependencies[i][0].text)

