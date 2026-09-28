import sys
import math


class CoefReader:

    def __init__(self, argv):
        self.argv = argv

    def read(self, index, name):
        prompt = f'Введите коэффициент {name}: '
        if index < len(self.argv):
            value = self.argv[index]
            print(prompt + value)
        else:
            value = input(prompt)
        while True:
            try:
                return float(value)
            except ValueError:
                print(f'Некорректное значение "{value}". Повторите ввод.')
                value = input(prompt)


class BiquadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = None
        self.roots = []
        self.infinite = False

    @staticmethod
    def _sqrt_roots(t):
        if t > 0:
            r = math.sqrt(t)
            return {-r, r}
        if t == 0:
            return {0.0}
        return set()

    def solve(self):
        a, b, c = self.a, self.b, self.c
        roots = set()
        if a == 0:
            if b == 0:
                self.infinite = (c == 0)
            else:
                roots = self._sqrt_roots(-c / b)
        else:
            self.discriminant = b * b - 4 * a * c
            if self.discriminant >= 0:
                sqrt_d = math.sqrt(self.discriminant)
                for t in ((-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)):
                    roots |= self._sqrt_roots(t)
        self.roots = sorted(roots)
        return self

    def __str__(self):
        lines = []
        if self.discriminant is not None:
            lines.append(f'Дискриминант D = {self.discriminant:g}')
        else:
            lines.append('A = 0: уравнение не является биквадратным, '
                         'решаем B*x^2 + C = 0')
        if self.infinite:
            lines.append('Бесконечно много корней (любое x)')
        elif not self.roots:
            lines.append('Нет действительных корней')
        else:
            lines.append(f'Количество действительных корней: {len(self.roots)}')
            lines += [f'  x{i} = {r:g}' for i, r in enumerate(self.roots, 1)]
        return '\n'.join(lines)


class App:

    def __init__(self, argv):
        self.reader = CoefReader(argv)

    def run(self):
        print('Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0')
        a = self.reader.read(1, 'А')
        b = self.reader.read(2, 'B')
        c = self.reader.read(3, 'C')
        print(BiquadraticEquation(a, b, c).solve())


if __name__ == '__main__':
    App(sys.argv).run()
