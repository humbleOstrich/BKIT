import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        print(f'{prompt} {coef_str}')
    except IndexError:
        coef_str = input(prompt + ' ')
    while True:
        try:
            return float(coef_str)
        except ValueError:
            print(f'Некорректное значение "{coef_str}". Повторите ввод.')
            coef_str = input(prompt + ' ')


def roots_from_square(t):
    if t > 0:
        r = math.sqrt(t)
        return [-r, r]
    if t == 0:
        return [0.0]
    return []


def get_roots(a, b, c):
    if a == 0:
        # Вырожденный случай: b*x^2 + c = 0
        if b == 0:
            return None, (None if c == 0 else [])
        return None, roots_from_square(-c / b)

    d = b * b - 4 * a * c
    if d < 0:
        return d, []
    sqrt_d = math.sqrt(d)
    t_values = {(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)}
    result = set()
    for t in t_values:
        result.update(roots_from_square(t))
    return d, sorted(result)


def print_result(d, roots):
    if d is not None:
        print(f'Дискриминант D = {d:g}')
    else:
        print('A = 0: уравнение не является биквадратным, решаем B*x^2 + C = 0')
    if roots is None:
        print('Бесконечно много корней (любое x)')
    elif len(roots) == 0:
        print('Нет действительных корней')
    else:
        print(f'Количество действительных корней: {len(roots)}')
        for i, r in enumerate(roots, 1):
            print(f'  x{i} = {r:g}')


def main():
    print('Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0')
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    d, roots = get_roots(a, b, c)
    print_result(d, roots)


if __name__ == '__main__':
    main()
