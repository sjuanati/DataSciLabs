"""
Available ufuncs: https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs
"""
import numpy as np


arr = np.arange(11)
print(arr)  # output: [ 0  1  2  3  4  5  6  7  8  9 10]

# 1) array with array:
print(arr + arr)  # output: [ 0  2  4  6  8 10 12 14 16 18 20]
print(np.add(arr, arr))  # output: [ 0  2  4  6  8 10 12 14 16 18 20]


# 2) array with scalar:
print(arr + 10)  # [10 11 12 13 14 15 16 17 18 19 20]
print(np.add(arr, 10))  # [10 11 12 13 14 15 16 17 18 19 20]


# 3) Aggregations functions such as sum, prod, cumsum, cumprod, max, min, mean, var, std have the following arguments:
"""
axis: which axis the operation should occur. For a 2D array, axis=0 means column-wise operation and
      axis=1 means row-wise operation.
dtype: This specifies the type of the returned array and of the accumulator in which the elements
       are summed (or multiplied, etc.).
out: This provides an alternative output array in which to place the result. It must have the same
       shape as the expected output, but the type of the output values will be cast if necessary.
keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions
       with size one. It ensures that the result has the same number of dimensions as the input.
initial: This is a starting value for this operation. For example, for sum, this would be the value
       from which the summation starts. By default, it starts from 0 for sum.
where: This is an array of the same shape as a (the input array), indicating whether a value should
       be included in the aggregation.
"""
arr0 = np.array([[1, 2], [3, 4], [5, 6]]) # output:
# [[1 2]
# [3 4]
# [5 6]]

# Product of columns for each row
print(arr0.prod(axis=1))
# output: [ 2 12 30]

# Product of columns for each row with keepdims=True
print(arr0.prod(axis=1, keepdims=True))
# output: 
# [[  2]
#  [ 12]
#  [ 30]]

# Sum with initial value
print(arr0.sum(initial=10))  # 31 (10 + 1 + 2 + 3 + 4 + 5 + 6)

# Sum only where the condition (element > 2) is True
print(arr0.sum(where=(arr0 > 2)))  # 18 (3 + 4 + 5 + 6)


# 4) universal array functions (mathematical operations to broadcast in the entire array)
np.set_printoptions(precision=2)  # limit decimals to 2
print(
    "sqr", np.sqrt(arr)
)  # output: [0. 1. 1.41 1.73 2. 2.24 2.45 2.65 2.83 3. 3.16] -> squared root
print(
    "exp", np.exp(arr)
)  # output: [1.00e+00 2.72e+00 7.39e+00 2.01e+01 5.46e+01 1.48e+02 4.03e+02 1.10e+03 2.98e+03 8.10e+03 2.20e+04] -> exponential
print("max", np.max(arr))  # output: 10 -> maximum value
print(
    "sin", np.sin(arr)
)  # output: [ 0. 0.84 0.91 0.14 -0.76 -0.96 -0.28 0.66 0.99 0.41 -0.54] -> sinus
print(
    "log", np.log(arr)
)  # output: [-inf 0. 0.69 1.1 1.39 1.61 1.79 1.95 2.08 2.2 2.3 ] -> logarithm (+Warning)
print("std", np.std(arr))  # output: 3.1622776601683795

# 5) Others:
# How to replace a NAN value by 0
arr2 = arr / arr
print(arr2)  # outout: [nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
arr2[np.isnan(arr2)] = 0
print(arr2)  # output: [0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
