import numpy as np 

arr = np.arange(0,11)

print(arr)

trozo_de_array = arr[0:6]

print(trozo_de_array)
# trozo_de_array[:] = 0
# print(trozo_de_array)
# print(arr)

arr_copy = arr.copy()
arr_copy[:] = 0

print(arr)
print(arr_copy)
