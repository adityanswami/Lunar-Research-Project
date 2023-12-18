import pandas as pd
crater_types = ["A", "C", "D", "All"]
for which_craters in crater_types:
    df = pd.read_excel(which_craters + " Crater Data.xlsx")
    crater_id_dict = {}
    for crater_id in set(df["Crater ID"]):
        max_pos = max(df.loc[df["Crater ID"] == crater_id]["Position"])
        crater_id_dict[crater_id] = max_pos
    for i in range(df.shape[0]):
        df.at[i, "Standardized Position"] = ((df["Position"][i])/crater_id_dict[df["Crater ID"][i]]) * 100
    df.to_excel(which_craters + " Crater Data.xlsx", index=False)