import np
from array import array

def get_unique_rows(x):
    #     Your code here
    uniq_arrays = set()
    for v in x:
        uniq_arrays.add(tuple(v))

    uniq_list = []
    for v in uniq_arrays:
        uniq_list.append(list(v))

    return uniq_list


x = np.random.randint(4, 6, size=(10, 3))
print(x)

print()
uniq = get_unique_rows(x)
print(uniq)
