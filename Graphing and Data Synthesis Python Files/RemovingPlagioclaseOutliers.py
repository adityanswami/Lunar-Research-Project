import numpy as np
import pandas as pd

df = pd.read_excel("All Crater Data Removing Plagioclase Outliers.xlsx")
list_of_rows = []

df.loc[(df["Iron Abundance"] < 8.5) & (df["Plagioclase Abundance"] <= 50), "Plagioclase Abundance"] = np.nan
df = df.dropna()

df.to_excel("All Crater Data Removing Plagioclase Outliers.xlsx")