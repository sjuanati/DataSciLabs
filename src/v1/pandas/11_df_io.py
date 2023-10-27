"""
Data Input/Output:
- CSV
- Excel
- HTML
- SQL
"""

import os
import pandas as pd

from sqlalchemy import create_engine

path = os.path.dirname(os.path.abspath(__file__)) + "/filez/"

# if data would be in ./data instead of ./src:
'''
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
users = os.path.join(data_dir, 'users.csv')
'''


# ********* CSV files ******************************

# store data from CSV file into a DataFrame
df = pd.read_csv(path + "data.csv")

# double check that columns are correctly loaded
df.columns

# save DataFrame into a CSV file
df.to_csv(path + "output.csv", index=False)


# ********* Excel files ****************************
# @dev: can only import data, not formulas, images, macros, etc

# 1) stores the first sheet from Excel into a DataFrame
df1 = pd.read_excel(path + "data.xlsx", sheet_name="Sheet1")

# 2) stores all sheets from Excel into a dictionary of DataFrames
df1 = pd.read_excel(path + "data.xlsx", sheet_name=None)

# 3) stores specific sheets from Excel into a dictionary of DataFrames
df1 = pd.read_excel(path + "data.xlsx", sheet_name=["Sheet1", "Sheet2"])

# 4)
df.to_excel(path + "output.xlsx", sheet_name="NewSheet")

# ********* H T M L files ***************************

# 1) stores
# @dev: reading html through pandas requires that Python is set up to trust
# the system's default set of certificates:
#   $ /Applications/Python\ 3.12/Install\ Certificates.command
# panda tries to read every table element from the html and creates a list of DataFrames
df3 = pd.read_html(
    "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
)
print(len(df))  # 1

# ********* S Q L  *********************************
# @dev: pandas isn't the best choice to read directly into a DB
engine = create_engine("sqlite:///:memory:")  # creates a light SQLite DB in memory
df.to_sql("my_table", engine)
sqldf = pd.read_sql("my_table", con=engine)

