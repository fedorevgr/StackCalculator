from math import sin, cos, tan, log2, log, e


class Arithmetics:
    def __init__(self, expression=None):
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
            'exp': self._e,
            'UM': self._UM
        }

    def _reset(self):
        self._stack = []
        self._expression = []

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

    def _e(self):
        self._stack[-1] = e ** self._stack[-1]

    def _UM(self):
        self._stack[-1] = -1 * self._stack[-1]

    def solve(self, equation=False):
        if equation:
            self._expression = equation

        for item in self._expression:
            if isinstance(item, float):
                self._stack.append(item)
            else:
                self._operations[item]()

        answer = self._stack[-1]

        self._reset()

        return answer


class Equation:
    def __init__(self, equation):
        self._base_equation = equation

        self.solver = Arithmetics()
        self._substituted = None

        self._left_bound = None
        self._right_bound = None

        self._opposite_signs = None

    def _substitute(self, value):
        self._substituted = self._base_equation.copy()

        for elem_id, elem in enumerate(self._substituted):
            if elem == 'x':
                self._substituted[elem_id] = value

    def _find_value_of(self, value):
        self._substitute(value)
        return self.solver.solve(equation=self._substituted)

    def find_solution(self, left_bound, right_bound):
        self._left_bound = left_bound
        self._right_bound = right_bound

        self._opposite_signs = (self._find_value_of(self._left_bound) * self._find_value_of(self._right_bound)) < 0

        if self._opposite_signs:
            print('\033[92mAlright, calculation might take some time so wait...\033[0m')
            intersection = -10000.0

            while abs(self._find_value_of(intersection)) > 0.0001:
                value_from_left_bound = self._find_value_of(self._left_bound)
                value_from_right_bound = self._find_value_of(self._right_bound)

                k = (value_from_left_bound - value_from_right_bound) / (self._left_bound - self._right_bound)
                b = value_from_right_bound - k * self._right_bound

                intersection = -(b / k)

                value_from_intersection = self._find_value_of(intersection)

                if value_from_left_bound * value_from_intersection > 0:
                    self._left_bound = intersection
                else:
                    self._right_bound = intersection

            if intersection == -0.0:
                intersection = 0.0

            return intersection
        else:
            print(f'\033[91mAre you sure that you want to find solutions to this equation in such bounds.\n'
                  f'As function values of bounds have the same sign, solving might take longer time. (y/n)\033[0m')

            if input() == 'y':
                x = self._left_bound

                while x < self._right_bound and abs(self._find_value_of(x)) > 0.00000001:
                    x += 0.00000001

                return x
            else:
                print('\033[91mOK\033[0m')
                return None

    def find_area(self, left, right):
        dx = 0.00001
        x = left

        area = 0

        while x < right:
            area += (self._find_value_of(x) + self._find_value_of(x + dx))
            x += dx

        area = area * dx / 2

        return area






