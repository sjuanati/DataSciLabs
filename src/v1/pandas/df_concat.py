import pandas as pd


"""
sign: pandas.concat(
        objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None,
        names=None, verify_integrity=False, sort=False, copy=True)
info: concatenates pandas objects (like DataFrames or Series) along a particular axis
      (either row-wise or column-wise).
args:
- objs: List or dict of pandas objects (DataFrames/Series) to be concatenated.
- axis: The axis to concatenate along. 0 for index (row-wise), 1 for columns (column-wise).
- join: How to handle overlapping columns. 'outer' for union and 'inner' for intersection.
- ignore_index: If True, don't use the index values along the concatenation axis.
- keys: Sequence to determine a hierarchical index or new levels to the columns, useful for
    concatenating DataFrames with different sources.
- levels: Specify levels to use for constructing a hierarchical index.
- names: Names for created hierarchical levels if keys is provided.
- verify_integrity: If True, checks that the new concatenated axis does not have duplicates.
- sort: Sort the non-concatenation axis if it's not already aligned.
- copy: If False, avoid copying data when possible.
"""

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
#    A  B
# 0  1  3
# 1  2  4
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
#    A  B
# 0  5  7
# 1  6  8


# Row-wise Concatenation of DataFrames
pd.concat([df1, df2])
#    A  B
# 0  1  3
# 1  2  4
# 0  5  7
# 1  6  8


# Row-wise Concatenation of DataFrames ignoring Indexes
pd.concat([df1, df2], ignore_index=True)
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8


# Column-wise Concatenation of DataFrames
df3 = pd.DataFrame({"C": [9, 10], "D": [11, 12]})
pd.concat([df1, df3], axis=1)
#    A  B   C   D
# 0  1  3   9  11
# 1  2  4  10  12
df4 = pd.DataFrame({"C": [9, 10], "D": [11, 12]}, index=[2, 3])
pd.concat([df1, df4], axis=1)
#      A    B     C     D
# 0  1.0  3.0   NaN   NaN
# 1  2.0  4.0   NaN   NaN
# 2  NaN  NaN   9.0  11.0
# 3  NaN  NaN  10.0  12.0


# Concatenating Using MultiIndex
pd.concat([df1, df2], keys=["df1", "df2"])
#        A  B
# df1 0  1  3
#     1  2  4
# df2 0  5  7
#     1  6  8


# Combining Series with DataFrames
s1 = pd.Series(["X", "Y"], name="Letters")
pd.concat([df1, s1], axis=1)
#    A  B Letters
# 0  1  3       X
# 1  2  4       Y


# Handling Overlapping Data with join
# @dev: When the DataFrames don't have the same set of columns, you can choose to take
#       the intersection (join='inner') or the union (join='outer').
df4 = pd.DataFrame({"B": [3, 4], "D": [5, 6]})
result_outer = pd.concat(
    [df1, df4], join="outer"
)  # This will have NaN values for unmatched columns
#      A  B    D
# 0  1.0  3  NaN
# 1  2.0  4  NaN
# 0  NaN  3  5.0
# 1  NaN  4  6.0
result_inner = pd.concat(
    [df1, df4], join="inner"
)  # This takes only the common columns, 'B' in this case
#    B
# 0  3
# 1  4
# 0  3
# 1  4
