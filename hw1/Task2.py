def format_case(x: str) -> str:
    is_space = False
    res = ''
    for v in x:
        if is_space:
            res += v.upper()
            is_space = False
        elif v.isupper():
            res += '_' + v.lower()
        elif v == '_':
            is_space = True
        else:
            res += v

    return res


print(format_case('helloWorld'))
print(format_case('helloWorldBlet'))
print(format_case('hello_world'))
print(format_case('hello_world_blet'))