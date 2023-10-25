import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(
    data=randn(5, 4), index=["A", "B", "C", "D", "E"], columns=["W", "X", "Y", "Z"]
)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# show all values greater than 0, NaN otherwise
df[df > 0]
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118       NaN       NaN  0.605965
# C       NaN  0.740122  0.528813       NaN
# D  0.188695       NaN       NaN  0.955057
# E  0.190794  1.978757  2.605967  0.683509

# show columns "X" & "Y" where values in column "W" > 0 and
df[df["W"] > 0][["X", "Y"]]
#           X         Y
# A  0.628133  0.907969
# B -0.319318 -0.848077
# D -0.758872 -0.933237
# E  1.978757  2.605967

# multiple conditions
# - each condition in parenthesis
# - don't use `and`, `or` but `&`, `|` instead
df[(df["W"] > 0) & (df["Y"] > 1)]
#           W         X         Y         Z
# E  0.190794  1.978757  2.605967  0.683509

# reset index
# if drop=True is not set, the new AND old indices are added
df.reset_index(drop=True)
#           W         X         Y         Z
# 0  2.706850  0.628133  0.907969  0.503826
# 1  0.651118 -0.319318 -0.848077  0.605965
# 2 -2.018168  0.740122  0.528813 -0.589001
# 3  0.188695 -0.758872 -0.933237  0.955057
# 4  0.190794  1.978757  2.605967  0.683509

# set a column as the DS index
# if we don't want to label the index row, use `df.index.name = None`
newind = "CA NY WY OR CO".split()  # ['CA', 'NY', 'WY', 'OR', 'CO']
df["States"] = newind
df_state = df.set_index("States")
#                W         X         Y         Z
# States
# CA      2.706850  0.628133  0.907969  0.503826
# NY      0.651118 -0.319318 -0.848077  0.605965
# WY     -2.018168  0.740122  0.528813 -0.589001
# OR      0.188695 -0.758872 -0.933237  0.955057
# CO      0.190794  1.978757  2.605967  0.683509

# @dev: using loc to select a single row from a DataFrame will return a Series with
#       the DataFrame's columns as the Series's index
df_state.loc["CA"]
# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826
# To get the result as the original column, keep the result as a DataFrame
df_state.loc[["CA"]]
#               W         X         Y         Z
# CA      2.70685  0.628133  0.907969  0.503826
