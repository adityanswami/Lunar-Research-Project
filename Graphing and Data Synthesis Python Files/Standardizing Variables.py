import pandas as pd
import numpy

crater_types = ["A", "C", "D", "All"]
x_Axes_List = ["Position", "Longitude", "Latitude", "Clinopyroxene Abundance", "FeO Abundance",
               "TerrainHeight", "Iron Abundance", "Olivine Abundance", "Orthopyroxene Abundance",
               "Plagioclase Abundance", "TerrainSlope", "Titanium Abundance"]
for which_craters in crater_types:
    for x in x_Axes_List:
        df = pd.read_excel(which_craters + " Crater Data.xlsx")
        crater_id_dict = {}
        other_dict = {}
        for crater_id in set(df["Crater ID"]):
            rang = df.loc[df["Crater ID"] == crater_id][x].max(numeric_only= True) - df.loc[df["Crater ID"] == crater_id][x].min(numeric_only= True)
            crater_id_dict[crater_id] = rang
            other_dict[crater_id] = df.loc[df["Crater ID"] == crater_id][x].min(numeric_only= True)
        for i in range(df.shape[0]):
            if (crater_id_dict[df["Crater ID"][i]] != 0):
                df.at[i, "Standardized " + x] = (((df[x][i])-other_dict[df["Crater ID"][i]])/crater_id_dict[df["Crater ID"][i]]) * 100
            else:
                df.at[i, "Standardized " + x] = 100
        df.to_excel(which_craters + " Crater Data.xlsx", index=False)