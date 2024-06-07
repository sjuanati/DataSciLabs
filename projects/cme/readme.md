# Lido stETH vs. CME ETH Futures

## 1) Data extraction

### 1.1) ETH futures
- **Data source**: CME files
- **Filters**:
    - CME ETH price in USD percentil < 0.99

### 1.2) Lido stETH:
- **Data source**:  https://dune.com/queries/3775348
- **Networks**: ethereum, arbitrum, polygon & optimism
- **Criteria**: get either stETH trades or wstETH trades (applying a rate conversion updated in a daily basis from https://dune.com/queries/3777723) from table `dex.trades` and do a price average of all trades per date from the above networks.
- **Remarks**: there is the `prices.usd` table in Dune but price is effectively updated every 5 minutes, so it doesn't work for the 1 minute timefrime analysis.
- **Filters**:
    - trade amount in USD > 1
    - stETH price in USD > 850
    - stETH price in USD < 5000
    - stETH price in USD percentil < 0.99

## 2) Data processing:

### 2.1) ETH futures
After downloading all CME files from their ftp server, run the following scripts from this [Github Repository](https://github.com/sjuanati/cme_eth_futures/tree/main/src):
- Retrieve `Entry Date CT` and `Price` from CME files and forward fill the price for every minute:
```
1-cme_build_1m_entry-date.py
```
- Convert date field from CT (Central Time) to UTC (Universal Time Coordinated):
```
2-cme_convert_ct_to_utc.py
```
- Generate a new file for the 5-minute timeframe by selecting all records where the time is a multiple of 5 minutes:
```
3-cme_build_5m.py
```
- Generate a new file for the 1-hour timeframe by selecting all records where the time is a multiple of 0 minutes:
```
4-cme_build_1h.py
```

### 2.2) Lido stETH:
After dumping all CSV file from the Dune query, run the following scripts from this [Github Repository](https://github.com/sjuanati/cme_eth_futures/tree/main/src):
- Forward fill the price for every minute:
```
8-steth_price_backfill.py
```
- Generate a new file for the 5-minute timeframe by selecting all records where the time is a multiple of 5 minutes:
```
9-steth_build_5m.py
```
- Generate a new file for the 1-hour timeframe by selecting all records where the time is a multiple of 0 minutes:
```
10-steth_build_1h.py
```
## 3) Outliers:

Lido's stETH & wstETH data from Dune has some cases where the price is considerably off without a clear reason and pattern. Despite most of them have been removed, there are still outliers in the current analysis as shown in the "Outliers hunting" section of the [notebook](https://github.com/sjuanati/DataSciLabs/blob/main/projects/cme/src/regression_all_tf.ipynb).

These outliers are identified by the standard deviation distance over the predicted price after applying a linear regression model. To further remove outliers, one option is to exclude from the datasets all those values that are over a certain standard deviation threshold.
