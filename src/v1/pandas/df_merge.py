import pandas as pd


"""
sign: pandas.merge(
        left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False,
        right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False,
        validate=None)
info: combines 2+ pandas DataFrames or Series based on common columns (similar to SQL joins)
args:
- left: Left DataFrame or named Series.
    The "base" data that you want to add columns to from a "right" DataFrame or Series.
- right: Right DataFrame or named Series.
    The data that you want to use to add columns to the "left" DataFrame or Series.
- how: Type of merge to be performed -> which keys are to be included in the resulting table
    (e.g., 'left', 'right', 'outer', 'inner').
- on: Column or index level names to join on.
    Column name that exists in both the "left" and "right" DataFrame to use as keys.
- left_on: Column or index level names to join on in the left DataFrame.
    Columns from the left DataFrame to use as keys if they don't exist in the right DataFrame.
- right_on: Column or index level names to join on in the right DataFrame.
    Columns from the right DataFrame to use as keys if they don't exist in the left DataFrame.
- left_index: Use the index from the left DataFrame as the join key(s).
    If True, use the index of the left DataFrame as its join key(s).
- right_index: Use the index from the right DataFrame as the join key(s).
    If True, use the index of the right DataFrame as its join key(s).
- sort: Sort the result DataFrame by the join keys in lexicographic order.
    If True, it will sort by the join keys.
- suffixes: Suffix to apply to overlapping column names in the left and right side.
    Tuple of (string, string) which gets appended to overlapping column names from left 
    and right DataFrames respectively.
- copy: Copy data from inputs.
    If False, avoid copying data into the resulting structure in some exceptional cases.
- indicator: Add a column to the output DataFrame called _merge with information on the source of each row.
    Can be either True or a string specifying the column's name. The column will have a Categorical
    type with values ('left_only', 'right_only', or 'both').
- validate: String that specifies validation of merged keys.
    For example, 'one_to_one', 'one_to_many', etc. It ensures merging is performed on specific criteria.
    If the criteria aren't met, an exception is raised.
"""

df1 = pd.DataFrame(
    {"A": ["A0", "A1", "A2", "A3"], "B": ["B0", "B1", "B2", "B3"], "key": [1, 2, 3, 4]}
)
#     A   B  key
# 0  A0  B0    1
# 1  A1  B1    2
# 2  A2  B2    3
# 3  A3  B3    4
df2 = pd.DataFrame(
    {"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"], "key": [3, 4, 5, 6]}
)
#     C   D  key
# 0  C0  D0    3
# 1  C1  D1    4
# 2  C2  D2    5
# 3  C3  D3    6


# Simple Join on a Single Column (key)
pd.merge(df1, df2, on="key")
#     A   B  key   C   D
# 0  A2  B2    3  C0  D0
# 1  A3  B3    4  C1  D1


# Left join
pd.merge(df1, df2, on="key", how="left")
#     A   B  key    C    D
# 0  A0  B0    1  NaN  NaN
# 1  A1  B1    2  NaN  NaN
# 2  A2  B2    3   C0   D0
# 3  A3  B3    4   C1   D1


# Right join
pd.merge(df1, df2, on="key", how="right")
#      A    B  key   C   D
# 0   A2   B2    3  C0  D0
# 1   A3   B3    4  C1  D1
# 2  NaN  NaN    5  C2  D2
# 3  NaN  NaN    6  C3  D3


# Outer join (+ replacing 'NaN' by 'N/A')
pd.merge(df1, df2, on="key", how="outer").fillna("N/A")
#      A    B  key    C    D
# 0   A0   B0    1  N/A  N/A
# 1   A1   B1    2  N/A  N/A
# 2   A2   B2    3   C0   D0
# 3   A3   B3    4   C1   D1
# 4  N/A  N/A    5   C2   D2
# 5  N/A  N/A    6   C3   D3


# Joining on Index
df1_idx = df1.set_index("key")
#       A   B
# key
# 1    A0  B0
# 2    A1  B1
# 3    A2  B2
# 4    A3  B3
df2_idx = df2.set_index("key")
#       C   D
# key
# 3    C0  D0
# 4    C1  D1
# 5    C2  D2
# 6    C3  D3
pd.merge(df1_idx, df2_idx, left_index=True, right_index=True)
#       A   B   C   D
# key
# 3    A2  B2  C0  D0
# 4    A3  B3  C1  D1


# Handling Overlapping Column Names
# @dev: The suffixes argument in pd.merge() is used to handle other overlapping column NAMES
#       that aren't part of the join criteria
df1["E"] = ["E0", "E1", "E2", "E3"]
#     A   B  key   E
# 0  A0  B0    1  E0
# 1  A1  B1    2  E1
# 2  A2  B2    3  E2
# 3  A3  B3    4  E3
df2["E"] = ["E4", "E5", "E6", "E7"]
#     C   D  key   E
# 0  C0  D0    3  E4
# 1  C1  D1    4  E5
# 2  C2  D2    5  E6
pd.merge(df1, df2, on="key", suffixes=("_left", "_right"))
#     A   B  key E_left   C   D E_right
# 0  A2  B2    3     E2  C0  D0      E4
# 1  A3  B3    4     E3  C1  D1      E5
pd.merge(df1, df2, on="key")
#     A   B  key E_x   C   D E_y
# 0  A2  B2    3  E2  C0  D0  E4
# 1  A3  B3    4  E3  C1  D1  E5
