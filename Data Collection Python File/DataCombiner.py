import pandas
import glob
import os
Crater_ID = input("Enter Crater ID: ")
files = os.path.join(Crater_ID + "\\" + "*.csv")
files = glob.glob(files)
basedf = pandas.read_csv(Crater_ID+"\\"+"quickmap-profile-data (0).csv")
df = pandas.DataFrame()
df['position'] = basedf['position']
df['lon'] = basedf['lon']
df['lat'] = basedf['lat']
for f in files:
    temp_df = pandas.read_csv(f)
    df = pandas.merge(df, temp_df, on=["position", "lon", "lat"], how="outer")
df.to_csv(Crater_ID+"\\"+Crater_ID+".csv", index=False)

