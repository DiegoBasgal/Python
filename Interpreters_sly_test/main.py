from sly import Lexer, Parser

#Lexer
class CalcLexer(Lexer):
    tokens = { ID, NUM, PLUS, TIMES, MINUS, DIVIDE, ATRIB, LPAREN, RPAREN, INTEIRO }
    ignore = ' \t'

    # Tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ATRIB = r'='
    LPAREN = r'\('
    RPAREN = r'\)'


    # Special cases
    ID['inteiro'] = INTEIRO

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


# Parser
class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE)
        )

    def __init__(self):
        print('Inicializando...')
        
# Grammar Rules
    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUM')
    def expr(self, p):
        return int(p.NUM)

diretorio = 'test.txt'
fp = open(diretorio,"r")
texto = fp.read()
fp.close

lexer = CalcLexer()
parser = CalcParser()

for tok in lexer.tokenize(texto):
        print('token=%r, lexema=%r' % (tok.type, tok.value))


result = parser.parse(lexer.tokenize(texto))
print(result)

        
