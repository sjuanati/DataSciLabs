import numpy as np
import pandas as pd

"""
Sign: pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
Info: A Series is similar to a one-dimensional NumPy array but with a key difference: it has an associated labeled index.
Args:
- data: Data to be stored in the Series. Can be many different types, like a Python dict, ndarray, scalar value, etc.
- index: The index (row labels) of the Series. Must be unique and hashable. The same length as data.
    Defaults to a range index (0, 1, 2, ...).
- dtype: Data type for the Series. If not specified, the dtype is inferred.
- name: Name for the Series, especially useful when the Series is later turned into a DataFrame with this Series as a column.
- copy: Copy input data.
Difs with numpy arrays:
- Index Labels: As mentioned, Series has labeled indices, while NumPy arrays have integer indices.
- Data Alignment: Operations between Series align data based on label, not position.
- Integrated Handling of Missing Data: Unlike a NumPy array, a Pandas Series can have multiple data types, and it handles
    missing data (NaN) more seamlessly.
- Mixed Data Types: A Series can contain any Python object and can have mixed data types, whereas NumPy arrays must have
    homogeneous data. 
"""

py_list_values = [10, 20, 30]
py_list_labels = ["a", "b", "c"]
py_dict = {"a": 10, "b": 20, "c": 30}
np_arr = np.array(py_list_values)

# Series creation from a py list without labels
s = pd.Series(data=py_list_values)
# 0    10
# 1    20
# 2    30
# dtype: int64

# Series creation from a py list with labels
s = pd.Series(data=py_list_values, index=py_list_labels)
s = pd.Series(py_list_values, py_list_labels)
# a    10
# b    20
# c    30
# dtype: int64

# Series creation from a numpy array with labels
s = pd.Series(np_arr, py_list_labels)
# a    10
# b    20
# c    30
# dtype: int64

# Series creation from a py dictionary
s = pd.Series(py_dict)
# a    10
# b    20
# c    30
# dtype: int64

# Series creation with multiple types
s = pd.Series(data=["a", 3, True])
# 0    a
# 1    3
# 2    True
# dtype: object

# Select element/s within the Series
s.loc[2]
# True
s[s == 'a']
# 0    a


# ************* Common use-cases *************
"""
Data Exploration and Cleaning:
- Detecting and filling missing values.
- Converting data types.
- String operations (capitalizing, lowercasing, stripping whitespace, etc.).
"""
s = pd.Series(["a", "b", None, "d"]).fillna("c")
# 0    a
# 1    b
# 2    None
# 3    d

"""
Time Series Analysis:
- Indexing data by timestamps and analyzing time series data.
"""
dates = pd.date_range("20231023", periods=6)
ts = pd.Series(np.random.randn(6), index=dates)
# 2023-10-23    0.132072
# 2023-10-24    0.584578
# 2023-10-25    0.688100
# 2023-10-26    0.624417
# 2023-10-27    1.151598
# 2023-10-28   -0.450089

"""
Arithmetic Operations:
- Simple arithmetic between Series (addition, subtraction, etc.) which aligns data by the Series' indices.
"""
s1 = pd.Series([1, 2, 4], index=["USA", "Germany", "Japan"])
s2 = pd.Series([1, 3, 4], index=["USA", "Catalunya", "Japan"])
print(s1 + s2)  # sum values that match by the label (and convert to float by default)
# Catalunya    NaN
# Germany      NaN
# Japan        8.0
# USA          2.0

"""
Aggregation and Statistical Operations:
- Calculating sum, mean, median, standard deviation, etc.
"""
s = pd.Series([1, 2, 3, 4, 5, 100])
s.mean()  # 19.6 -> (1+2+3+4+5+100)/5
s.median()  # 3.5 -> middle number from ordered dataset (or avg of two in the middle if even dataset)
s.std()  # 39,6

"""
Boolean Indexing:
- Filtering data based on certain conditions.
"""
s = pd.Series([1, 2, 3, 4, 5])
even_values = s[s % 2 == 0]
# 1    2
# 3    4

"""
Conversion:
- Converting Series to other data structures like dictionaries, lists, or arrays.
"""
s = pd.Series({"a": 1, "b": 2, "c": 3}).to_dict()
# {'a': 1, 'b': 2, 'c': 3}

"""
Handling Categorical Data:
- Series can represent categorical data efficiently, which can be useful for data analysis tasks
  or when preparing data for machine learning.
"""
s = pd.Series(["cat", "dog", "cat", "bird"], dtype="category")
# 0     cat
# 1     dog
# 2     cat
# 3    bird
# dtype: category
# Categories (3, object): ['bird', 'cat', 'dog']

"""
Vectorized Operations:
- Applying functions to Series without the need for explicit loops.
"""
s = pd.Series([1, 2, 3])
squared = s.apply(lambda x: x**2)
# 0    1
# 1    4
# 2    9

"""
Sorting and Ranking:
- Sorting data by index or values.
- Ranking entries.
"""
s = pd.Series([3, 1, 2], index=["c", "a", "b"])
sorted_by_index = s.sort_index()
sorted_by_values = s.sort_values()
print(sorted_by_index)
# a    1
# b    2
# c    3
print(sorted_by_values)
# a    1
# b    2
# c    3
