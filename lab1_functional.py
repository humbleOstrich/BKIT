import sys
import math
from functools import reduce


def to_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def read_coef(name, value=None):
    prompt = f'Введите коэффициент {name}: '
    match value, to_float(value):
        case None, _:
            return read_coef(name, input(prompt))
        case _, None:
            print(f'Некорректное значение "{value}". Повторите ввод.')
            return read_coef(name, input(prompt))
        case _, number:
            return number


def sqrt_roots(t):
    match t:
        case t if t > 0:
            return {-math.sqrt(t), math.sqrt(t)}
        case 0 | 0.0:
            return {0.0}
        case _:
            return set()


def solve(a, b, c):
    match (a, b, c):
        case (0, 0, 0):
            return None, None
        case (0, 0, _):
            return None, []
        case (0, _, _):
            return None, sorted(sqrt_roots(-c / b))
        case _:
            d = b * b - 4 * a * c
            match d:
                case d if d < 0:
                    return d, []
                case _:
                    ts = map(lambda s: (-b + s * math.sqrt(d)) / (2 * a), (1, -1))
                    roots = reduce(lambda acc, t: acc | sqrt_roots(t), ts, set())
                    return d, sorted(roots)


def format_result(result):
    d, roots = result
    head = ('A = 0: уравнение не является биквадратным, решаем B*x^2 + C = 0'
            if d is None else f'Дискриминант D = {d:g}')
    match roots:
        case None:
            body = ['Бесконечно много корней (любое x)']
        case []:
            body = ['Нет действительных корней']
        case [*rs]:
            body = [f'Количество действительных корней: {len(rs)}'] + \
                   [f'  x{i} = {r:g}' for i, r in enumerate(rs, 1)]
    return '\n'.join([head, *body])


def main(argv):
    print('Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0')
    args = argv[1:4] + [None] * (3 - len(argv[1:4]))

    def from_arg(name, v):
        match v:
            case str():
                print(f'Введите коэффициент {name}: {v}')
        return read_coef(name, v)

    a, b, c = map(lambda p: from_arg(*p), zip(('А', 'B', 'C'), args))
    print(format_result(solve(a, b, c)))


if __name__ == '__main__':
    main(sys.argv)
