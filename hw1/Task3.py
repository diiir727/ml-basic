import re
import math


def kvadr(x: str):
    match = re.fullmatch(r'(.*\d*)\*x\*\*2 (.) (\d*)\*x (.) (\d*) = 0', x)
    if not match:
        raise Exception('Неверный формат строки')

    a = int(match[1])
    b = int(match[2] + match[3])
    c = int(match[4] + match[5])

    d = b * b - 4 * a * c

    if d < 0:
        return []
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return [x1, x2]
    else:
        x = -b / (2 * a)
        return [x]


y = '1*x**2 + 2*x - 3 = 0'
print(kvadr(y))