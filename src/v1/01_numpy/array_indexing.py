import numpy as np

arr = np.arange(11)
print(arr)  # output : [ 0  1  2  3  4  5  6  7  8  9 10]

# array slice (same as python lists)
# arr[row:column] -> from row included | until column excluded
print(arr[:5])  # output: [0 1 2 3 4]
print(arr[5:])  # output: [ 5  6  7  8  9 10]
print(arr[1:5])  # output: [1 2 3 4]

# broadcast values. CAREFUL!!! numpy arrays are 👹 MUTABLE
arr_slice = arr[:6]  # assigns [0 1 2 3 4 5] to arr_slice
arr_slice[:] = 99  # assings 99 to all positions
print(arr_slice)  # output: [99 99 99 99 99 99]
print(arr)  # output: [99 99 99 99 99 99  6  7  8  9 10] !!!!!
# to avoid mutability:
arr_copy = arr.copy()  # copies [99 99 99 99 99 99  6  7  8  9 10] to arr_copy
arr_copy[:] = 1
print(arr)  # output: [99 99 99 99 99 99  6  7  8  9 10] -> remains the same
print(arr_copy)  # output: [1 1 1 1 1 1 1 1 1 1 1] -> changed

# access 2D-arrays (matrices)
arr2 = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# [[5, 10, 15], 
#  [20, 25, 30], 
#  [35, 40, 45]]
# double bracket notation:
print(arr2[2][1]) # output: 40 (row 2, column 1)
# comma notation:
print(arr2[2,1]) # output: 40 (row 2, column 1)
# colon notation:
print(arr2[:2,1:]) # output: (until row 1, from column 1)
# [[10 15]
#  [25 30]]
print(arr2[:,2]) # output: [15 30 45] (for all rows, column 2)
# exercise: select values marked in *
arr4 = np.arange(50).reshape(5,10) 
print(arr4)
# [[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 *13 *14 15 16 17 18 19]
# [20 21 22 *23 *24 25 26 27 28 29]
# [30 31 32 33 34 35 36 37 38 39]
# [40 41 42 43 44 45 46 47 48 49]]
print(arr4[1:3,3:5])
print(arr4[-4:-2, -7:-5])

# conditional selection
arr3 = np.arange(11)
bool_arr = arr3 > 5
print(bool_arr) # output: [False False False False False False  True  True  True  True  True]
print(arr3[bool_arr]) # output: [ 6  7  8  9 10]
print(arr3[arr3>5]) # output: [ 6  7  8  9 10] * most common
