import math


def amulet_area(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


assert amulet_area(3, 4, 5) == 6