import np

my_array = np.random.randint(0, 50, (5, 6))
max1 = np.max(my_array)

print(f'max: {max1}')
print('Shape: ', my_array.shape)
print('\nArray')
print(my_array)

max_col = 0
for v in my_array:
    for j, vv in enumerate(v):
        if vv == max1:
            max_col = j
            break

print(f"\nmax col index: {max_col}")
for v in my_array:
    print(v[max_col])


