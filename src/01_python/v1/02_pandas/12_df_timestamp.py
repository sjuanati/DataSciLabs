import pandas as pd

df = pd.DataFrame(
    {
        "ts": [
            "2023-11-26 19:31:00",
            "2023-11-26 20:40:00",
            "2023-12-15 09:16:12",
            "2023-12-31 23:56:08",
        ]
    }
).rename_axis("key")
# key   ts
# 0     2023-11-26 19:31:00
# 1     2023-11-26 20:40:00
# 2     2023-12-15 09:16:12
# 3     2023-12-31 23:56:08

# type for `ts` is currently str:
type(df["ts"].iloc[0])
# <class 'str'>

# convert str to datetime
df["ts"] = pd.to_datetime(df["ts"])

# convert datetime to unix timestamp (using int to avoid decimal notation)
df["unix_ts"] = df["ts"].apply(lambda x: int(x.timestamp()))
# key     ts                  unix_ts
# 0       2023-11-26 19:31:00  1701027060
# 1       2023-11-26 20:40:00  1701031200
# 2       2023-12-15 09:16:12  1702631772
# 3       2023-12-31 23:56:08  1704066968

# show day, month, year..
df_item = df["ts"].iloc[0]
print(
    df_item.day,
    df_item.month,
    df_item.year,
    df_item.hour,
    df_item.minute,
    df_item.second,
    df_item.dayofweek,
)
# 26 11 2023 19 31 0 6

# create 3 columns for Hour & Day of the Week
# merge -> only 2 DataFrames at a time
dmap = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
df_hour = df["ts"].apply(lambda x: x.hour).to_frame("hour").rename_axis("key")
df_day_of_week = (
    df["ts"].apply(lambda x: dmap[x.dayofweek]).to_frame("dayofweek").rename_axis("key")
)
df_merge = pd.merge(pd.merge(df, df_hour, on="key"), df_day_of_week, on="key")
# key ts                     unix_ts    hour    dayofweek
# 0   2023-11-26 19:31:00    1701027060 19       Sun
# 1   2023-11-26 20:40:00    1701031200 20       Thu
# 2   2023-12-15 09:16:12    1702631772 9        Tue
# 3   2023-12-31 23:56:08    1704066968 23       Thu

# add/subtract time:
# Timedelta -> weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds
t = df["ts"].iloc[0]  # 2023-11-26 19:31:00
t + pd.Timedelta(hours=3)  # +3 hours -> 2023-11-26 22:31:00
t - pd.Timedelta(minutes=40)  # -40 mins -> 2023-11-26 18:51:00
t - pd.Timedelta(seconds=5)  # -5 mins -> 2023-11-26 19:30:55
t + pd.Timedelta(days=2)  # +2 days -> 2023-11-28 19:31:00
t - pd.Timedelta(weeks=1)  # -1 week -> 2023-11-19 19:31:00
# DateOffset -> years, months, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds
t + pd.DateOffset(months=2)  # -2 months -> 2024-01-26 19:31:00
t + pd.DateOffset(years=2)  # -2 years -> 2025-11-26 19:31:00

# count records by day
count = df.groupby(df['ts'].dt.date).count()['ts']
# ts
# 2023-11-26    2
# 2023-12-15    1
# 2023-12-31    1

# count records by month
count = df.groupby(df['ts'].dt.month).count()['ts']
# ts
# 11    2
# 12    2
