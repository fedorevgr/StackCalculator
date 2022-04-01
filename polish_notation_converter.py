class Converter:
    weights = {
        '(': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
        '^': 4,
        ')': 5
    }

    def __init__(self, expression):
        stack = []
        output = []
        for token in expression:
            if isinstance(token, float):
                output.append(token)
            elif token in list('+-*/^'):



