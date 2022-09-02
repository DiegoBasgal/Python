from sly import Lexer, Parser

class CalcLexer(Lexer):
    tokens = { ID, NUM, PLUS, TIMES, MINUS, DIVIDE, ATRIB, LPAREN, RPAREN, ENDMARKER, LESS, GREATER, EQUAL, QUOTE, COLON, INTEIRO, PARA, INICIO, FIM_SE, FIM_PARA, IMPRIMA, ENTAO, SENAO, LEIA, FIM, PASSO, ATE, AND, OR, LESSEQUAL, GREATEREQUAL, NOTEQUAL, SE}
    ignore = ' \t'

    # Tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'\d+'
    LPAREN = r'\('
    RPAREN = r'\)'
    QUOTE = r'\"'
    COLON = r'\:'
    ENDMARKER = r'\;'
    #Aritmetics
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    #Atribuition
    ATRIB = r'<-'
    #Relational
    NOTEQUAL = r'<>'
    LESSEQUAL = r'<='
    GREATEREQUAL = r'>='
    LESS = r'\<'
    GREATER = r'\>'
    EQUAL = r'\='


    # Special cases
    ID['se'] = SE
    ID['fim_se'] = FIM_SE
    ID['inicio'] = INICIO
    ID['inteiro'] = INTEIRO
    ID['entao'] = ENTAO
    ID['senao'] = SENAO
    ID['leia'] = LEIA
    ID['imprima'] = IMPRIMA
    ID['para'] = PARA
    ID['fim_para'] = FIM_PARA
    ID['fim'] = FIM
    ID['passo'] = PASSO
    ID['ate'] = ATE
    #Lógics
    ID['e'] = AND
    ID['ou'] = OR

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1



diretorio = 'test.txt'
fp = open(diretorio,"r")
texto = fp.read()
fp.close

lexer = CalcLexer()

for tok in lexer.tokenize(texto):
        print('token=%r, lexema=%r' % (tok.type, tok.value))
