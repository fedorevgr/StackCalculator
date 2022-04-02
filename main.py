from src.lexer import Lexer
from src.polish_notation_converter import Converter
from src.solver import Arithmetics


while True:
    #  test = '21.34+sin(3^ln(6))*2'
    lexer = Lexer().parse(input('Enter your expression: '))
    print(lexer)
    if lexer:
        reverse_notation = Converter().convert(lexer)
        solver = Arithmetics(reverse_notation)
        print(solver.solve())
