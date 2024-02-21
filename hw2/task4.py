import math

import np
from numpy import dot
from numpy.linalg import norm


def cal_euclidean(a, b):
    sum = 0
    for idx, x in enumerate(a):
        sum += math.pow(x - b[idx], 2)

    return math.sqrt(sum)


def cal_manhattan(a, b):
    distance = 0
    for idx, x in enumerate(a):
        distance += math.fabs(x - b[idx])

    return distance


def cal_cosine(a, b):
    return dot(a, b) / (norm(a) * norm(b))


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))
