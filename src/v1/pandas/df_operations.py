import numpy as np
import pandas as pd


df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4],
        "col2": [444, 555, 666, 444],
        "col3": ["abc", "def", "ghi", "xyz"],
    }
)
#    col1  col2 col3
# 0     1   444  abc
# 1     2   555  def
# 2     3   666  ghi
# 3     4   444  xyz

# count total unique values in a column
df["col2"].nunique()
# 3

# count unique values per colum
df["col2"].value_counts()
# col2
# 444    2
# 555    1
# 666    1

# select data with conditional selections
df[(df["col1"] > 2) & (df["col2"] == 444)]
#    col1  col2 col3
# 3     4   444  xyz


# apply method for functions
def times2(x):
    return x * 2


df["col1"].apply(times2)
df["col1"].apply(lambda x: x * 2)
# 0    2
# 1    4
# 2    6
# 3    8

# remove columns
df.drop("col1", axis=1)
#    col2 col3
# 0   444  abc
# 1   555  def
# 2   666  ghi
# 3   444  xyz

# show DataFrame data:
df.columns
# Index(['col1', 'col2', 'col3'], dtype='object')
df.index
# RangeIndex(start=0, stop=4, step=1)

# sort columns - keeps the indices
df.sort_values("col2")
#    col1  col2 col3
# 0     1   444  abc
# 3     4   444  xyz
# 1     2   555  def
# 2     3   666  ghi

# null values
df.isnull()
#     col1   col2   col3
# 0  False  False  False
# 1  False  False  False
# 2  False  False  False
# 3  False  False  False

# null values per column
df.isnull().sum()
# col1    0
# col2    0
# col3    0

# null values in DataFrame
df.isnull().sum().sum()
# 0

"""
sign: pandas.DataFrame.pivot(self, index=None, columns=None, values=None)
info: reshapes data based on column values, essentially turning unique values from one column
    into multiple columns in the DataFrame
args:
- index : str or object, optional. Column to use to make the new frame’s index.
- columns : str or object. Column to use to make the new frame’s columns.
- values : str or object, optional. Column to use for populating new frame’s values.
"""

data = {
    "A": ["foo", "foo", "foo", "bar", "bar", "bar"],
    "B": ["one", "one", "two", "two", "one", "one"],
    "C": ["x", "y", "x", "y", "x", "y"],
    "D": [1, 3, 2, 5, 4, 1],
}
df = pd.DataFrame(data)
#      A    B  C  D
# 0  foo  one  x  1
# 1  foo  one  y  3
# 2  foo  two  x  2
# 3  bar  two  y  5
# 4  bar  one  x  4
# 5  bar  one  y  1

df_pivot = df.pivot_table(values="D", index=["A", "B"], columns=["C"])
print(df_pivot)
# C          x    y
# A   B
# bar one  4.0  1.0
#     two  NaN  5.0
# foo one  1.0  3.0
#     two  2.0  NaN
