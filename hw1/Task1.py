def format_str(x: str) -> str:
    i = 0
    res = ''
    for v in x[::-1]:
        i += 1
        res += v
        if i % 3 == 0:
            res += ' '

    return res[::-1].strip()


print(format_str('123'))
print(format_str('12354654'))