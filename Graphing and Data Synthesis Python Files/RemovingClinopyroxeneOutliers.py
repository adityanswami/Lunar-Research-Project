import numpy as np
import pandas as pd

df = pd.read_excel("All Crater Data Clinopyroxene Outliers Removed.xlsx")
list_of_rows = []

for i in range(len(df["Iron Abundance"])):
    if ((df["Iron Abundance"].iloc[i] >= 3.5) and (df["Iron Abundance"].iloc[i] <= 7.5)):
        if (df["Clinopyroxene Abundance"].iloc[i] >= 30):
            list_of_rows.append(i)
    elif ((df["Iron Abundance"].iloc[i] > 7.5) and (df["Iron Abundance"].iloc[i] <= 8.6)):
        if (df["Clinopyroxene Abundance"].iloc[i] >= 35):
            list_of_rows.append(i)
    print (i/len(df["Iron Abundance"]))
df = df.drop(list_of_rows)
df.to_excel("All Crater Data Clinopyroxene Outliers Removed.xlsx")