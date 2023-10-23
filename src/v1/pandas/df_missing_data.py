import numpy as np
import pandas as pd

"""
sign: DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
info: remove missing values (NaNs) from a DataFrame or Series.
args:
- axis: Whether to drop rows (0 or 'index') or columns (1 or 'columns') containing missing values.
- how: Strategy to drop: 'any' drops rows/columns with at least one NaN, 'all' drops rows/columns where all values are NaN.
- thresh: Minimum number of non-missing values required to keep a row/column.
- subset: List of columns to consider when dropping rows.
- inplace: Whether to modify the original DataFrame (True) or return a new one (False).
"""

d = {"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  NaN  2
# 2  NaN  NaN  3

# drop rows with missing values
df.dropna()
#      A    B  C
# 0  1.0  5.0  1

# drop columns with missing values
df.dropna(axis=1)
#    C
# 0  1
# 1  2
# 2  3

# drop columns with N+ missing values
df.dropna(thresh=2)
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  NaN  2

"""
sign: DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
info: fill missing values (NaNs) in a DataFrame or Series with specified values.
args:
- value: Scalar, dictionary, Series, or DataFrame. Value to use to fill missing values.
- method: Method to fill gaps: 'ffill' (propagate last valid observation forward) or 
    'bfill' (use next valid observation to fill gap).
- axis: Whether to fill missing values along rows (0 or 'index') or columns (1 or 'columns').
- inplace: Whether to modify the original DataFrame (True) or return a new one (False).
- limit: Maximum number of consecutive missing values to forward/backward fill.
- downcast: Downcast data types if possible (e.g., float to int).
"""

# fill all nulls with a value
df.fillna(value="RS")
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0   RS  2
# 2   RS   RS  3

# fill nulls with the mean of the column
df["A"].fillna(value=df["A"].mean())
# 0    1.0
# 1    2.0
# 2    1.5

# fill nulls using a dictionary
dict = {"A": 10, "B": 20, "C": 30}
df.fillna(value=dict)
#       A     B  C
# 0   1.0   5.0  1
# 1   2.0  20.0  2
# 2  10.0  20.0  3

# fill nulls with previous or next filled column value
# - With ffill, for every NaN cell, it takes the last valid (non-NaN) value from the same column and
#   fills the NaN with it. If the NaN is the first entry of the column (like in column 'B'), it remains
#   unfilled since there's no prior value.
# - With bfill, the NaN cells are filled with the next valid (non-NaN) value from the same column.
#   It's the opposite of ffill.
df.fillna(method="ffill")
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  5.0  2
# 2  2.0  5.0  3

# fill N consecutive null values with a given value
# - fills NaN values with 0, but only for one consecutive NaN in the column. If there are more than one
#   consecutive NaNs in a column, only the first one gets filled.
df.fillna(value=0, limit=1)
#      A    B  C
# 0  1.0  5.0  1
# 1  2.0  0.0  2
# 2  0.0  NaN  3
