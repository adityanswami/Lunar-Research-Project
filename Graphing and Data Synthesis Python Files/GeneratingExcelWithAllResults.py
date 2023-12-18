import pandas as pd
import numpy
import scipy

crater_types = ["A", "C", "D", "All"]
mHBoth = ["maria", "highlands", "both"]
x_Axes_List = ["Position", "Longitude", "Latitude", "Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight",
               "Iron Abundance", "Olivine Abundance", "Orthopyroxene Abundance", "Plagioclase Abundance",
               "TerrainSlope", "Titanium Abundance"]
y_Axes_List = ["Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight", "Iron Abundance", "Olivine Abundance",
               "Orthopyroxene Abundance", "Plagioclase Abundance", "TerrainSlope", "Titanium Abundance"]
count = 0
total = len(crater_types)*len(mHBoth)*len(x_Axes_List)*len(y_Axes_List)


results = pd.DataFrame({"Label": [], "R Value": [], "R^2 Value": []})

for eachtype in crater_types:
    for geography in mHBoth:
        for y_value in y_Axes_List:
            if (eachtype == "A") and (geography == "maria"):
                break
            for x_value in x_Axes_List:
                which_craters = eachtype
                mariaOrHighlands = geography
                x_Axis = x_value
                y_Axis = y_value
                df = pd.read_excel(which_craters + " Crater Data.xlsx")
                x = df[x_Axis]
                y = df[y_Axis]
                z = df["Crater ID"]
                if mariaOrHighlands == "maria":
                    x = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    new_row = {"Label": y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands, "R Value": rvalue, "R^2 Value": (rvalue**2)}
                    results.loc[len(results)] = new_row
                elif mariaOrHighlands == "highlands":
                    x = numpy.array(df.loc[df["Highlands?"] == "highlands"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "highlands"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    new_row = {"Label": y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands,
                               "R Value": rvalue, "R^2 Value": (rvalue ** 2)}
                    results.loc[len(results)] = new_row
                else:
                    x = numpy.array(df[x_Axis])
                    y = numpy.array(df[y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    new_row = {"Label": y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands,
                               "R Value": rvalue, "R^2 Value": (rvalue ** 2)}
                    results.loc[len(results)] = new_row
                count += 1
                print(count/total)

results.to_excel("Correlation Results.xlsx", sheet_name="Correlation Results", index=False)