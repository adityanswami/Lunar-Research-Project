import numpy as np
import pandas as pd

df = pd.read_excel("All Crater Data Removing FeO and Titanium Outliers.xlsx")
list_of_rows = []

df.loc[(df["Titanium Abundance"] > 6), "Titanium Abundance"] = np.nan
df = df.dropna()

df.to_excel("All Crater Data Removing FeO and Titanium Outliers.xlsx")