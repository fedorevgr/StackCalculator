class Converter:
    def __init__(self):
        self.weights = {
            '(': 1,
            '+': 2,
            '-': 2,
            '*': 3,
            '/': 3,
            '^': 4,
            'sin': 4,
            'cos': 4,
            'tan': 4,
            'cot': 4,
            'log': 4,
            'ln': 4,
            '-sin': 4,
            '-cos': 4,
            '-tan': 4,
            '-cot': 4,
            '-log': 4,
            '-ln': 4,
        }

        self.operations = ['+', '-', '*', '/', '^']

        self.functions = ['sin', 'cos', 'tan', 'cot', 'log', 'ln', '-sin', '-cos', '-tan', '-cot', '-log', '-ln']

        self.consts = ['pi', 'e', '-pi', '-e', 'x', '-x']

    def convert(self, expression):
        stack = []
        output = []
        for token in expression:
            if isinstance(token, float) or token in self.consts:
                output.append(token)
            else:
                if not stack:
                    stack.append(token)
                    continue

                if token in self.functions:
                    stack.append(token)

                elif token == '(':
                    stack.append(token)

                elif token == ')':
                    while stack[-1] != "(":
                        output.append(stack.pop())
                    stack.pop()

                elif token in self.operations:

                    if self.weights[stack[-1]] >= self.weights[token]:
                        while stack and self.weights[stack[-1]] >= self.weights[token]:
                            output.append(stack.pop())

                    stack.append(token)

        while stack:
            output.append(stack.pop())

        return output






