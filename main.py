from lexer import Lexer


while True:
    #  test = '21.34+sin(3^ln(6))*2'
    lexer = Lexer().parse(input('Enter yor expression: '))
    if lexer:
        print(lexer)
