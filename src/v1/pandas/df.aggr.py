import pandas as pd


data = {
    "Company": ["AAPL", "AAPL", "NVDA", "NVDA", "TSLA", "TSLA"],
    "Person": ["Sergi", "Charlie", "Mat", "Vanessa", "Marc", "Elena"],
    "Sales": [200, 120, 340, 124, 243, 350],
}

df = pd.DataFrame(data)
#   Company   Person  Sales
# 0    AAPL    Sergi    200
# 1    AAPL  Charlie    120
# 2    NVDA      Mat    340
# 3    NVDA  Vanessa    124
# 4    TSLA     Marc    243
# 5    TSLA    Elena    350

# average sales by company
df.groupby("Company")["Sales"].mean()
# Company
# AAPL    160.0
# NVDA    232.0
# TSLA    296.5

# average sales for Tesla
df.groupby("Company")["Sales"].mean().loc["TSLA"]
# 296.5

# company stats
df.groupby("Company").describe()
#         Sales
#         count   mean         std    min     25%    50%     75%    max
# Company
# AAPL      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
# NVDA      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
# TSLA      2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0

# multiple aggregations at once
df.groupby("Company")["Sales"].agg(["mean", "sum", "max"])
#           mean  sum  max
# Company
# AAPL     160.0  320  200
# NVDA     232.0  464  340
# TSLA     296.5  593  350

# custom aggregation
df.groupby("Company")["Sales"].agg(lambda x: x.max() - x.min())
# AAPL     80
# NVDA    216
# TSLA    107
