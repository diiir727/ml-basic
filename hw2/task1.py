def share_bread(N, K):
    y = K % N
    x = (K - y) / N
    return x, y


print(share_bread(N=3, K=14))
# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)
