import numpy as np
from numpy.random import randint


# ******** 1) ARRAY CONVERSION *******************
"""
convert lists to numpy array
"""
list = [1, 2, 3]
arr = np.array(list)
print(f"list: {list} \n arr: {arr} \n")

list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = np.array(list2)
print(f"list: {list2} \n arr: {arr2} \n")

# ******** 2) ARRAY CREATION *******************

"""
np.arange(start, stop, step, dtype=None)
-> returns evenly spaced values within a given interval. Values are generated within the half-open
   interval [start, stop) (in other words, the interval including start but excluding stop)
start: Start of interval. Default is 0.
stop: End of interval.
step: Spacing between values. Default is 1.
dtype: Data type of the result. If not provided, inferred from other input arguments.
"""
arr3 = np.arange(0, 11, 2)
print(arr3)
# output: [ 0  2  4  6  8 10]


"""
np.zeros(shape, dtype=float, order='C')
-> returns a new array of given shape and type, filled with zeros.
shape: Shape of the new array (e.g., (2, 3) for a 2x3 matrix).
dtype: Data type of the returned array. Default is float.
order: Whether to store multidimensional data in row-major (C-style)
       or column-major (Fortran-style) order in memory.
"""
arr4 = np.zeros(3, dtype=int)
print(arr4)
# output: [0 0 0]


"""
np.ones(shape, dtype=None, order='C')
-> returns a new array of given shape and type, filled with ones.
shape: Shape of the new array.
dtype: Data type of the returned array. Default is float.
order: Whether to store multidimensional data in row-major (C-style)
       or column-major (Fortran-style) order in memory.
"""
arr5 = np.ones((2, 3))
print(arr5)
# output:
# [[1. 1. 1.]
#  [1. 1. 1.]]


"""
np.full(shape, fill_value, dtype=None, order='C')
-> returns a new array of given shape and type, filled with `fill_value`.
shape: Shape of the new array.
fill_value: Fill value.
dtype: Data type of the returned array. If not provided, inferred from the
       type of fill_value.
order: Whether to store multidimensional data in row-major (C-style)
       or column-major (Fortran-style) order in memory.
"""
arr6 = np.full((2, 2), 4.5)
print(arr6)
# output:
# [[4.5 4.5]
#  [4.5 4.5]]


"""
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
-> returns evenly spaced numbers over a specified range
start: The starting value of the sequence.
stop: The end value of the sequence.
num: (Optional) The number of evenly spaced samples to generate. Default is 50.
endpoint: (Optional) If True (default), stop is the last value in the range. If False, the range ends before stop.
retstep: (Optional) If True, return the step size between values.
dtype: (Optional) The type of the output array.
axis: (Optional) The axis in the result along which the linspace samples are stored.
"""
arr7 = np.linspace(0, 10, 5)
print(arr7)
# output: [ 0.0  2.5  5.0  7.5  10.0 ]


"""
np.eye(N, M=None, k=0, dtype=<class 'float'>)
creates a 2-D identity matrix, where the diagonal elements are ones, and all off-diagonal elements are zeros.
N: Number of rows in the output.
M: (Optional) Number of columns in the output. If None, defaults to N.
k: (Optional) The position of the diagonal. 0 (the default) refers to the main diagonal. A value greater 
    than 0 refers to an upper diagonal, and a value less than 0 to a lower diagonal.
"""
I = np.eye(3)
print(I)
# output:
#   [[1. 0. 0.]
#    [0. 1. 0.]
#    [0. 0. 1.]]


"""
np.random.rand(d0, d1, ..., dn)
-> generates an array of random numbers that are uniformly distributed over the range [0, 1). 
   This means the numbers generated can be as small as 0 but are always less than 1.
d0, d1, ..., dn (optional): Dimensions of the returned array. If no dimensions are provided,
    a single random number is generated.
"""
arr8 = np.random.rand(2, 3)
print(arr8)
# output:
# [[0.05477668 0.98760856 0.21679442]
#  [0.73299024 0.98000816 0.64418181]]


"""
np.random.randn(d0, d1, ..., dn)
-> generates an array of random numbers that are sampled from a standard normal (or Gaussian) distribution.
   This distribution is centered around 0 and has a standard deviation of 1.
d0, d1, ..., dn (optional): Dimensions of the returned array. If no dimensions are provided,
   a single random number is generated.
"""
arr9 = np.random.randn(5)
print(arr9)
# output: [ 1.06754886 -0.11510802 -0.61316595  0.70482481 -0.05808373]


"""
np.random.randint(low, high=None, size=None, dtype='l')
-> returns an ndarray (N-dimensional array) or scalar (if size is not provided) of random integers
   from the specified range
low (int): The lowest (inclusive) integer in the range. If high is not provided, then this is the exclusive upper bound, and the lower bound is 0.
high (int, optional): The exclusive upper bound of the range. If not provided, the generated integers will be between 0 and low.
size (int or tuple of ints, optional): Determines the shape of the output array. If not provided, a single integer is returned.
dtype (data-type, optional): Desired data-type of the result. Default is int64.
"""
arr10 = np.random.randint(1, 11, 5)
print(arr10)
# output: [ 9  4  2  8 10]
arr101 = randint(1, 11, 5)  # because of `from numpy.random import randint`
print(arr101)


# ******** 3) ARRAY METHODS *******************

"""
ndarray.reshape(shape, order='C')
gives a new shape to an array without changing its data
shape: Tuple of ints. The new shape should be compatible with the original shape. If an integer, then the result will be a 1D array of that length.
       One shape dimension can be -1. In this case, the value is inferred from the length of the array and the remaining dimensions.
order: {‘C’, ‘F’, ‘A’, ‘K’}, optional. Specifies the memory layout of the reshaped array. Default is 'C'.
    'C': Row-major order (C-style).
    'F': Column-major order (Fortran-style).
    'A': Memory layout if it preserves the input order.
    'K': Memory layout of input array.
"""
arr = np.array([1, 2, 3, 4])
arr11 = arr.reshape(2, 2)
print(arr11)
# output:
# [[1 2]
#  [3 4]]
arr = np.array([1, 2, 3, 4, 5, 6])
arr12 = arr.reshape(2, -1)
print(arr12)
# output:
# [[1 2 3]
#  [4 5 6]]
arr = np.array([[1, 2], [3, 4], [5, 6]])
arr13 = arr.reshape(-1)
print(arr13)
# Output: [1 2 3 4 5 6]


"""
ndarray.max(axis=None, out=None, keepdims=False)
ndarray.min(axis=None, out=None, keepdims=False)
-> returns the maximum/minumum value from an array.
axis: Axis along which to operate. By default, flattened input is used.
out: Alternative output array in which to place the result.
keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size one.
"""
arr14 = np.arange(0, 11)
print(arr14.max())  # output : 10
print(arr14.min())  # output : 0


"""
ndarray.argmax(axis=None, out=None)
ndarray.argmin(axis=None, out=None)
-> returns the indices of the maximum/minimum values along an axis.
axis: Axis along which to operate. By default, flattened input is used.
out: Alternative output array in which to place the result.
"""
# Create a 3x3 matrix
matrix = np.array([[1, 3, 7], [4, 0, 8], [2, 5, 6]])
# [[1, 3, 7],
#  [4, 0, 8],
#  [2, 5, 6]]]

# Using argmax with axis=0 (Find the index of the maximum value in each column)
col_max_indices = matrix.argmax(axis=0)
print(col_max_indices)  # Output: [1 2 1]

# Using argmax with axis=1 (Find the index of the maximum value in each row)
row_max_indices = matrix.argmax(axis=1)
print(row_max_indices)  # Output: [2 2 2]

# Using out parameter
output_array = np.zeros(3, dtype=int)  # An array to store the results
matrix.argmax(axis=0, out=output_array)
print(output_array)  # Output: [1 2 1]


"""
ndarray.dtype
-> describes the type of the elements in an array
no params (it's an attribute instead of method)
"""
print(matrix.dtype)
# output: int64




"""
The `list` and `arr` in your provided code are different types of data structures, and they have significant differences:

1. Type:
   - `list` is a Python built-in list.
   - `arr` is a NumPy array (specifically an `ndarray` object).

2. Functionality:
   - Python lists are general-purpose containers. They can contain items of different types, are dynamically sized, and 
     support typical list operations like appending, removing, etc.
   - NumPy arrays, on the other hand, are homogeneous (all elements must be of the same type) and are static in size 
     (once created, you can't change their size without creating a new array). Their strength lies in efficient operations
     over all elements of the array and are specifically tailored for numerical operations and mathematical computations.

3. Memory:
   - NumPy arrays are more memory efficient than Python lists, especially for large data sets.

4. Performance:
   - NumPy arrays are faster than Python lists for operations like element-wise addition, multiplication, etc. This is because
     NumPy is implemented in C and optimized for performance.

5. Operations:
   - With Python lists, you can't directly perform element-wise operations without loops. For example, you can't multiply
     two lists directly.
   - With NumPy arrays, you can perform element-wise operations, matrix multiplications, and much more without needing loops. 

6. Flexibility:
   - Python lists are more flexible in terms of types of elements they can contain. A single list can contain an integer, a
     string, a float, another list, etc.
   - NumPy arrays require that all elements be of the same type.

7. Size:
   - The size of a Python list can be changed (you can append, insert, or remove elements).
   - The size of a NumPy array is fixed upon creation.

Here's an illustrative difference:

```
# For a Python list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # This concatenates the two lists: [1, 2, 3, 4, 5, 6]

# For a NumPy array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)  # This adds the arrays element-wise: [5, 7, 9]
```

In summary, while they might look similar and can be used in some common scenarios, Python lists and NumPy arrays are designed
for different purposes and have distinct characteristics and capabilities.
"""
