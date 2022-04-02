from math import sin, cos, tan, log2, log


class Arithmetics:
    def __init__(self, expression):
        self._stack = []
        self._expression = expression
        self._operations = {
            '+': self._sum,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide,
            '^': self._expo,
            'sin': self._sin,
            'cos': self._cos,
            'tan': self._tan,
            'cot': self._cot,
            'log': self._log,
            'ln': self._ln,
            'UM': self._UM
        }

    def _sum(self):
        self._stack[-2] = self._stack[-2] + self._stack[-1]
        del self._stack[-1]

    def _subtract(self):
        self._stack[-2] = self._stack[-2] - self._stack[-1]
        del self._stack[-1]

    def _multiply(self):
        self._stack[-2] = self._stack[-2] * self._stack[-1]
        del self._stack[-1]

    def _divide(self):
        self._stack[-2] = self._stack[-2] / self._stack[-1]
        del self._stack[-1]

    def _expo(self):
        self._stack[-2] = self._stack[-2] ** self._stack[-1]
        del self._stack[-1]

    def _sin(self):
        self._stack[-1] = sin(self._stack[-1])

    def _cos(self):
        self._stack[-1] = cos(self._stack[-1])

    def _tan(self):
        self._stack[-1] = tan(self._stack[-1])

    def _cot(self):
        self._stack[-1] = 1 / (tan(self._stack[-1]))

    def _log(self):
        self._stack[-1] = log2(self._stack[-1])

    def _ln(self):
        self._stack[-1] = log(self._stack[-1])

    def _UM(self):
        self._stack[-1] = -1 * self._stack[-1]

    def solve(self):
        for item in self._expression:
            if isinstance(item, float):
                self._stack.append(item)
            else:
                self._operations[item]()

        return self._stack[-1]
