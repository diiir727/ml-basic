def encrypt(x: str, offset: int):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    res = ''
    for c in x:
        res += alphabet[(alphabet.index(c) + offset) % len(alphabet)]

    return res


print(encrypt('hello ska', 1))