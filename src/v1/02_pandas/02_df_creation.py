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

# create DataFrame from arrays:
df0 = pd.DataFrame({"Number": range(1500), "Squared": [i**2 for i in range(1500)]})
#   Number	Squared
# 0	    0	    0
# 1	    1	    1
# 2	    2	    4
# 3	    3	    9

df1 = pd.DataFrame(randn(5, 4))
#           0         1         2         3
# 0  2.706850  0.628133  0.907969  0.503826
# 1  0.651118 -0.319318 -0.848077  0.605965
# 2 -2.018168  0.740122  0.528813 -0.589001
# 3  0.188695 -0.758872 -0.933237  0.955057
# 4  0.190794  1.978757  2.605967  0.683509

# create DataFrame from Series and assign name to index:
s = pd.Series(data=[10, 20, 30, 40])
df10 = s.to_frame("values").rename_axis('ind')
# ind      values
# 0        10
# 1        20
# 2        30
# 3        40

df1.shape
# (5, 4) => this is why index=0 is rows and index=1 is columns

df1.head(2)  # shows first 2 rows (Default: 5)

df1.tail(3)  # shows last 3 rows (Default: 5)

len(df1.columns)  # shows how many columns: 4

len(df1.index)  # shows how many rows: 5

df1.info()  # DataFrame overview
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   0       5 non-null      float64
#  1   1       5 non-null      float64
#  2   2       5 non-null      float64
#  3   3       5 non-null      float64
# dtypes: float64(4)
# memory usage: 292.0 bytes

df1.describe() # DataFrame figures on numeric fields
#               0         1         2         3
# count  5.000000  5.000000  5.000000  5.000000
# mean  -0.318858  0.583606 -0.019461  0.306431
# std    1.332007  0.391326  1.487830  0.702163
# min   -2.034974  0.189756 -1.366002 -0.414400
# 25%   -0.824430  0.191037 -1.000617 -0.396331
# 50%   -0.802687  0.593870 -0.621900  0.405658
# 75%    0.999963  0.940041  0.602127  0.779087
# max    1.067838  1.003325  2.289089  1.158140

# seed: to force the same random values (repeat every time a random num is generated)
np.random.seed(101)
df = pd.DataFrame(
    data=randn(5, 4), index=["A", "B", "C", "D", "E"], columns=["W", "X", "Y", "Z"]
)
#           W         X         Y         Z
# A  0.302665  1.693723 -1.706086 -1.159119
# B -0.134841  0.390528  0.166905  0.184502
# C  0.807706  0.072960  0.638787  0.329646
# D -0.497104 -0.754070 -0.943406  0.484752
# E -0.116773  1.901755  0.238127  1.996652

# show one column -> returns a Serie
df["W"]
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794

# show column type: every DataFrame column is always a pandas Series
type(df["W"])
# <class 'pandas.core.series.Series'>

# show column type (for strings, it will return object type: `dtype('O')`)
df['W'].dtypes
# dtypes: float64(4)  # (4) -> means there are 4 columns with this type

# show column type based on a value
type(df['W'].iloc[0])
# dtypes: float64(4) 

# show a list of columns -> returns a DataSet
df[["W", "Z"]]
#           W         Z
# A  2.706850  0.503826
# B  0.651118  0.605965
# C -2.018168 -0.589001
# D  0.188695  0.955057
# E  0.190794  0.683509

# show a row by label
df.loc["A"]
# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826

# show a row by index
df.iloc[0]
# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826

# show a value
df.loc["B", "Y"]  # shows row 'B' column 'Y'
# -0.848

# show a subset of data
(df.loc[["A", "B"], ["W", "Y"]])
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
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# drop a row
df.drop("E", inplace=True)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
