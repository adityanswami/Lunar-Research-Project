import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
import seaborn
import time
import numpy
import scipy

crater_types = ["A", "C", "D", "All"]
mHBoth = ["maria", "highlands", "both"]
x_Axes_List = ["Standardized Position", "Longitude", "Latitude", "Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight",
               "Iron Abundance", "Olivine Abundance", "Orthopyroxene Abundance", "Plagioclase Abundance",
               "TerrainSlope", "Titanium Abundance"]
y_Axes_List = ["Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight", "Iron Abundance", "Olivine Abundance",
               "Orthopyroxene Abundance", "Plagioclase Abundance", "TerrainSlope", "Titanium Abundance"]
count = 0
total = len(crater_types)*len(mHBoth)*len(x_Axes_List)*len(y_Axes_List)

filtered = []
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


                elif mariaOrHighlands == "highlands":

                    x = numpy.array(df.loc[df["Highlands?"] == "highlands"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "highlands"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])


                else:

                    x = numpy.array(df[x_Axis])
                    y = numpy.array(df[y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])

                if ((rvalue**2) < 0.49) and ((rvalue**2) >= 0.25):
                    filtered.append(y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands + "\t" + str(rvalue) + "\t" + str(rvalue**2) + "\n")

                count += 1
                print(count/total)

file = open("Nonstandardized R between 0.7 and 0.5.txt", 'w')
file.writelines(filtered)
file.close()


