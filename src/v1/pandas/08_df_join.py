import pandas as pd

"""
sign: DataFrame.join(self, other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
info: combine columns of two potentially differently-indexed DataFrames into a single DataFrame.
    It is similar to SQL's JOIN operation and is a convenient method to combine DataFrames,
    especially when the DataFrames have different indices.
args:
- other: The DataFrame or Series to join with the current DataFrame.
- on: The column or index level to use as the join key in the calling DataFrame.
- how: Join type; one of ['left', 'right', 'outer', 'inner'] ** DEFAULTS TO 'left' **
- lsuffix: Suffix to add to overlapping column names from the left DataFrame.
- rsuffix: Suffix to add to overlapping column names from the right DataFrame.
- sort: Whether to sort the resulting join keys. Defaults to False.
"""


df1 = pd.DataFrame(
    {"A": ["A0", "A1", "A2", "A3"], "B": ["B0", "B1", "B2", "B3"], "key": [1, 2, 3, 4]}
).set_index("key")
#     A   B  key
# 0  A0  B0    1
# 1  A1  B1    2
# 2  A2  B2    3
# 3  A3  B3    4
df2 = pd.DataFrame(
    {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"], "key": [3, 4, 5, 6]}
).set_index("key")
#     C   D  key
# 0  C0  D0    3
# 1  C1  D1    4
# 2  C2  D2    5
# 3  C3  D3    6
df3 = pd.DataFrame(
    {"E": ["E0", "E1", "E2", "E3"], "A": ["A5", "A6", "A7", "A8"], "key": [1, 2, 3, 4]}
).set_index("key")
#     E   F  key
# 0  E0  F0    1
# 1  E1  F1    2
# 2  E2  F2    3
# 3  E3  F3    4


# Basic Join on Column (key):
df1.join(df2)
#       A   B    C    D
# key
# 1    A0  B0  NaN  NaN
# 2    A1  B1  NaN  NaN
# 3    A2  B2   C0   D0
# 4    A3  B3   C1   D1


# Outer Join on Index
df1.join(df2, how="outer")
#        A    B    C    D
# key
# 1     A0   B0  NaN  NaN
# 2     A1   B1  NaN  NaN
# 3     A2   B2   C0   D0
# 4     A3   B3   C1   D1
# 5    NaN  NaN   C2   D2
# 6    NaN  NaN   C3   D3


# Joining Multiple DataFrames
# @dev: Suffixes not supported when joining multiple DataFrames
# Case 1: No columns overlap
# df1.join([df2, df3])
#       A   B    C    D   E   F
# key
# 1    A0  B0  NaN  NaN  E0  F0
# 2    A1  B1  NaN  NaN  E1  F1
# 3    A2  B2   C0   D0  E2  F2
# 4    A3  B3   C1   D1  E3  F3
# Case 2: Columns overlap
df1.join(df2, how="outer", lsuffix="_df1", rsuffix="_df2").join(
    df3, how="outer", lsuffix="_df1", rsuffix="_df3"
)
#     A_df1    B    C    D    E A_df3
# key
# 1      A0   B0  NaN  NaN   E0    A5
# 2      A1   B1  NaN  NaN   E1    A6
# 3      A2   B2   C0   D0   E2    A7
# 4      A3   B3   C1   D1   E3    A8
# 5     NaN  NaN   C2   D2  NaN   NaN
# 6     NaN  NaN   C3   D3  NaN   NaN


# Join with Overlapping Columns using lsuffix and rsuffix
df1.join(df3, lsuffix="_left", rsuffix="_right")
#     A_left   B   E A_right
# key
# 1       A0  B0  E0      A5
# 2       A1  B1  E1      A6
# 3       A2  B2  E2      A7
# 4       A3  B3  E3      A8
