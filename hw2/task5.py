import np


my_array = np.random.rand(100)
max1 = np.max(my_array)
min1 = np.min(my_array)
print(max1, min1)
print(my_array)

for idx, v in enumerate(my_array):
    if v == max1:
        my_array[idx] = 0
    if v == min1:
        my_array[idx] = 1


print(np.max(my_array), np.min(my_array))




