from lexer import Lexer
from polish_notation_converter import Converter


while True:
    #  test = '21.34+sin(3^ln(6))*2'
    lexer = Lexer().parse(input('Enter yor expression: '))
    print(lexer)
    if lexer:
        print(Converter().convert(lexer))
