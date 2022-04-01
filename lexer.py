import string

class Lexer:
    _OPERATIONS = '+-*/^'

    def convert_numbers_from(self):
        for item_id in range(len(self._result)):
            if self._result[item_id][0].isdigit():
                self._result[item_id] = float(self._result[item_id])

    def __init__(self):
        self._state = 'S'
        self._buffer = ''
        self._index = 0
        self._current_char = ''
        self._brackets_count = 0
        self._is_function = False
        self._result = []

        self._machine = {
            'S': self._state_s,  # default state
            'I': self._state_i,  # integer state
            'R': self._state_r,  # real number state
            'B': self._state_b,  # closing brackets state
            'F': self._state_f,  # function state
            'X': self._state_x   # variable state
        }

        self._expectations = {
            'S': 'number, letter, unary minus or opening bracket',
            'I': 'number, operator, comma or closing bracket',
            'R': 'number, operator or closing bracket',
            'B': 'operator or closing bracket',
            'F': 'letter or opening bracket',
            'X': 'closing bracket or operator',
            'B_ERR': 'right brackets count'
        }

    def _reset(self):
        self._state = 'S'
        self._buffer = ''
        self._index = 0
        self._current_char = ''
        self._brackets_count = 0
        self._is_function = False
        self._result = []

    def _flush_buffer(self):
        self._result.append(self._buffer)
        self._buffer = ''

    def _add_char_to_buffer(self):
        self._buffer += self._current_char

    def _flush_current_char(self):
        self._result.append(self._current_char)

    def _state_s(self):  # from default to default, I, F or X
        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'
        if self._current_char == '(':
            self._brackets_count += 1
            self._flush_current_char()
            return 'S'
        if self._current_char == '-':
            self._add_char_to_buffer()
            return 'S'

        if self._current_char in string.ascii_lowercase and self._current_char != 'x':
            self._add_char_to_buffer()
            return 'F'

        if self._current_char == 'x':
            self._add_char_to_buffer()
            self._flush_buffer()
            return 'X'

    def _state_i(self):  # from integer to integer, real or brackets
        if self._current_char == '.':
            self._add_char_to_buffer()
            return 'R'

        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'

        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_buffer()
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_r(self):  # from real to continue real or end number input
        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'

        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_buffer()
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_b(self):
        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_f(self):
        if self._current_char in string.ascii_lowercase:
            self._add_char_to_buffer()
            return 'F'

        if self._current_char == '(':
            self._brackets_count += 1
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_x(self):
        self._is_function = True

        if self._current_char == ')':
            self._flush_current_char()
            self._brackets_count -= 1
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def parse(self, expression: str):
        if not expression:
            print(f'\033[93mError\nEmpty expression\n'
                  f'\033[0m')
            return None

        for index, char in enumerate(expression):
            self._index = index
            self._current_char = char

            for_error = self._state

            self._state = self._machine[self._state]()

            if self._state is None:
                print(f'\033[93mError\nExpected {self._expectations[for_error]}\n'
                      f'{expression}\n{"~" * (index - 1)}^{"~" * (len(expression) - index)}\033[0m')
                return None

        if self._state not in 'IBX':
            print(f'\033[93mError\nCan not end with operator or function without arguments\n'
                  f'{expression}\n{"~" * (len(expression) - 1)}^\033[0m')
            return None

        to_del = []
        for item_id in range(len(self._result)):
            if not self._result[item_id]:
                to_del.append(item_id)

        for item in to_del:
            del self._result[item]

        self.convert_numbers_from()

        out = self._result

        if self._brackets_count != 0:
            brackets = []
            if self._brackets_count > 0:
                for elem_id in range(len(expression)):
                    if expression[elem_id] == '(':
                        brackets.append(elem_id)
                    elif expression[elem_id] == ')':
                        brackets.pop()
            elif self._brackets_count < 0:
                for elem_id in range(len(expression), 0, -1):
                    if expression[elem_id] == ')':
                        brackets.append(elem_id)
                    elif expression[elem_id] == '(':
                        brackets.pop()

            error = brackets[-1]

            print(f'\033[93mError\nBracket not closed, expected ")"\n{expression}\n'
                  f'{"~" * error}^{"~" * (len(expression) - error - 1)}\033[0m')

            return None

        self._flush_buffer()
        self._reset()

        return out




