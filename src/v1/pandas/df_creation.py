import numpy as np
import pandas as pd

from numpy.random import randn

"""
sign: pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
info: store and manipulate two-dimensional, size-mutable, and heterogeneous tabular data (data with
      rows and columns). It is essentially a table, much like a spreadsheet or SQL table.
args:
- data: data to be stored in the DataFrame (dict, list, another DataFrame, a NumPy array...)
- index: Default is None, which means it will use the default integer index (0, 1, 2, ...). For the row labels,
    the index to use for the resulting frame.
- columns: for the column labels, the columns to use for the resulting frame.
- dtype: data type to force for all columns. Only a single dtype is allowed. If None, infer.
- copy: whether to copy data from inputs. Default is False. If set to True, it will create copies of input data,
    ensuring that the original data is not modified.
"""

# each column is actually a pandas Series
df1 = pd.DataFrame(randn(5, 4))
print(df1)
#           0         1         2         3
# 0  2.706850  0.628133  0.907969  0.503826
# 1  0.651118 -0.319318 -0.848077  0.605965
# 2 -2.018168  0.740122  0.528813 -0.589001
# 3  0.188695 -0.758872 -0.933237  0.955057
# 4  0.190794  1.978757  2.605967  0.683509

print(df1.shape)
# (5, 4) => this is why index=0 is rows and index=1 is columns

np.random.seed(
    101
)  # to force the same random values (repeat every time a random num is generated)
df = pd.DataFrame(
    data=randn(5, 4), index=["A", "B", "C", "D", "E"], columns=["W", "X", "Y", "Z"]
)
print(df)
#           W         X         Y         Z
# A  0.302665  1.693723 -1.706086 -1.159119
# B -0.134841  0.390528  0.166905  0.184502
# C  0.807706  0.072960  0.638787  0.329646
# D -0.497104 -0.754070 -0.943406  0.484752
# E -0.116773  1.901755  0.238127  1.996652

# show one column -> returns a Serie
print(df["W"])
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
print(type(df["W"]))
# <class 'pandas.core.series.Series'>

# show a list of columns -> returns a DataSet
print(df[["W", "Z"]])
#           W         Z
# A  2.706850  0.503826
# B  0.651118  0.605965
# C -2.018168 -0.589001
# D  0.188695  0.955057
# E  0.190794  0.683509

# show a row by label
print(df.loc["A"])
# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826

# show a row by index
print(df.iloc[0])
# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826

# show a value
print(df.loc["B", "Y"])  # shows row 'B' column 'Y'
# -0.848

# show a subset of data
print((df.loc[["A", "B"], ["W", "Y"]]))
#           W         Y
# A  2.706850  0.907969
# B  0.651118 -0.848077

# add new column based on existing ones
df["new"] = df["W"] + df["Y"]
#           W         X         Y         Z       new
# A  2.706850  0.628133  0.907969  0.503826  3.614819
# B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
# C -2.018168  0.740122  0.528813 -0.589001 -1.489355
# D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
# E  0.190794  1.978757  2.605967  0.683509  2.796762

# drop a column
# without the inplace=True, the original DS is not modified
df.drop("new", axis=1, inplace=True)
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# drop a row
df.drop("E", inplace=True)
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
