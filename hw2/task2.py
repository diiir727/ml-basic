def leap_year(year):
    text_result = 'YOU SHALL NOT PASS'
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        text_result = 'YOU SHALL PASS'
    return text_result


assert leap_year(5) == 'YOU SHALL NOT PASS'
assert leap_year(104) == 'YOU SHALL PASS'
assert leap_year(116) == 'YOU SHALL PASS'
assert leap_year(200) == 'YOU SHALL NOT PASS'
