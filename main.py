from src.lexer import Lexer
from src.polish_notation_converter import Converter
from src.solver import Arithmetics, Equation


while True:
    #  test = 21.34+sin(3^ln(6))*2
    #  1+2-3*4/58^6-(-x)^-97+(-1.1)
    #  1+2-3*4/58^6-(-8)^-97+(-1.1)

    lexer = Lexer()
    expression = lexer.parse(input('Enter your expression: '))

    if expression:
        reverse_notation = Converter().convert(expression)

        if not lexer.is_function:

            solver = Arithmetics(reverse_notation)
            solution = solver.solve()

            print(solution)
        else:
            equation = Equation(reverse_notation)
            print('To solve equation you need to define the sector in which you what to find solution.')
            left = float(input('Enter the left bound of sector -> '))
            right = float(input('Enter the right bound of sector -> '))

            solution = equation.find_solution(left, right)
            print(f'\033[92mFound this in sector -> {solution}\033[0m')

            integration = input('Do you want to integrate? (y/n) ')
            if integration == 'y':
                print('To integrate you need to set bounds.')
                left = float(input('Enter the left bound -> '))
                right = float(input('Enter the right bound -> '))
                print(f'\033[92mHere is your area -> {equation.find_area(left, right)}.\033[0m')
            else:
                print('\033[92mAlright.\033[0m')

