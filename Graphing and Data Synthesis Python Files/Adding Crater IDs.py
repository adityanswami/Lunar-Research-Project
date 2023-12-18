import pandas as pd
column = "Crater ID"
which_crater = ["A", "C", "D"]



for type in which_crater:
    df = pd.read_excel(type + " Crater Data.xlsx")
    for i in range(len(df[column])):
        if (pd.isnull(df[column][i])== False):
            currentID = df[column][i]
        elif pd.isnull(df[column][i]):
            df.at[i, column] = currentID
    df.to_excel(type + " Crater Data.xlsx", index=False)