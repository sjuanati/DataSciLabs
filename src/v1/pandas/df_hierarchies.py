import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

# Index levels
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]

hier_index = list(zip(outside, inside))
# [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

hier_index = pd.MultiIndex.from_tuples(hier_index)
# MultiIndex([('G1', 1),
#             ('G1', 2),
#             ('G1', 3),
#             ('G2', 1),
#             ('G2', 2),
#             ('G2', 3)],
#            )

df = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
print(df)
#              A         B
# G1 1  2.706850  0.628133
#    2  0.907969  0.503826
#    3  0.651118 -0.319318
# G2 1 -0.848077  0.605965
#    2 -2.018168  0.740122
#    3  0.528813 -0.589001

# set index names
df.index.names = ["Groups", "Num"]
print(df)
#                    A         B
# Groups Num
# G1     1    2.706850  0.628133
#        2    0.907969  0.503826
#        3    0.651118 -0.319318
# G2     1   -0.848077  0.605965
#        2   -2.018168  0.740122
#        3    0.528813 -0.589001

# select subset
print(df.loc["G1"])
#             A         B
# Num
# 1    2.706850  0.628133
# 2    0.907969  0.503826
# 3    0.651118 -0.319318

# select subset
print(df.loc["G1"].loc[1])
# A    2.706850
# B    0.628133

# select one specific cell
print(df.loc["G2"].loc[2]["B"])
# 0.740122

# cross-section: select all values where Num=1
print(df.xs(1, level="Num"))
