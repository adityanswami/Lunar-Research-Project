import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
import seaborn
import time
import numpy
import scipy

plt.rcParams.update({"font.size": 25})
crater_types = ["A", "C", "D", "All"]
mHBoth = ["maria", "highlands", "both"]
# ["Standardized Position", "Standardized Longitude", "Standardized Latitude", "Standardized Clinopyroxene Abundance", "Standardized FeO Abundance", "Standardized TerrainHeight",
#                "Standardized Iron Abundance", "Standardized Olivine Abundance", "Standardized Orthopyroxene Abundance", "Standardized Plagioclase Abundance",
#                "Standardized TerrainSlope", "Standardized Titanium Abundance"]
x_Axes_List = ["Plagioclase Abundance"]
y_Axes_List = ["FeO Abundance"]
count = 0
total = len(crater_types)*len(mHBoth)*len(x_Axes_List)*len(y_Axes_List)
markers = {
    "maria": ".",
    "highlands": "^"
}

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
                colors = seaborn.color_palette(n_colors=len(set(df["Crater ID"])))
                colors_dict = dict((k, v) for k, v in enumerate(colors))
                crater_id_dict = pd.DataFrame(set(df["Crater ID"]))[0].to_dict()
                crater_id_dict = dict((v, k) for k, v in crater_id_dict.items())
                x = df[x_Axis]
                y = df[y_Axis]
                z = df["Crater ID"]
                numbered_crater_id = df["Crater ID"].map(crater_id_dict)
                if mariaOrHighlands == "maria":
                    x = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    resids = []
                    ys = [0] * len(x)
                    xs = [0] * len(y) * 2
                    yas = []
                    for element in y:
                        yas.append(element)
                        yas.append(-1 * element)
                    for i in range(len(x)):
                        resids.append(y[i] - (intercept + slope * x[i]))
                    plt.scatter(df.loc[df["Highlands?"] == "maria"][x_Axis],
                                resids,
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["maria"], facecolors="None", label="Datapoints from Maria Craters")
                    plt.plot(x, ys, color="black")
                    plt.plot(xs, yas, color="black")
                elif mariaOrHighlands == "highlands":
                    x = numpy.array(df.loc[df["Highlands?"] == "highlands"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "highlands"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    resids = []
                    ys = [0] * len(x)
                    xs = [0] * len(y) * 2
                    yas = []
                    for element in y:
                        yas.append(element)
                        yas.append(-1*element)
                    for i in range(len(x)):
                        resids.append(y[i]-(intercept + slope * x[i]))
                    plt.scatter(df.loc[df["Highlands?"] == "highlands"][x_Axis],
                                resids,
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["highlands"], facecolors="None", label="Datapoints from Highlands Craters")
                    plt.plot(x, ys, color="black")
                    plt.plot(xs, yas, color="black")
                else:
                    x = numpy.array(df[x_Axis])
                    y = numpy.array(df[y_Axis])
                    x_highlands = numpy.array(df.loc[df["Highlands?"] == "highlands"][x_Axis])
                    y_highlands = numpy.array(df.loc[df["Highlands?"] == "highlands"][y_Axis])
                    x_maria = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                    y_maria = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])

                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    resid_highlands = []
                    resid_maria = []
                    ys = [0] * len(x)
                    xs = [0] * len(y) * 2
                    yas = []
                    for element in y:
                        yas.append(element)
                        yas.append(-1 * element)
                    for i in range(len(x_highlands)):
                        resid_highlands.append(y_highlands[i] - (intercept + slope * x_highlands[i]))
                    for i in range(len(x_maria)):
                        resid_maria.append(y_maria[i] - (intercept + slope * x_maria[i]))
                    plt.scatter(df.loc[df["Highlands?"] == "highlands"][x_Axis],
                                resid_highlands,
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["highlands"], facecolors="None", label="Datapoints from Highlands Craters")
                    plt.scatter(df.loc[df["Highlands?"] == "maria"][x_Axis],
                                resid_maria,
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["maria"], facecolors="None", label="Datapoints from Maria Craters")
                    plt.plot(x, ys, color="black")
                    plt.plot(xs, yas, color="black")
                plt.legend(loc="best")
                plt.xlabel(x_Axis)
                plt.ylabel("Residuals")
                plt.title("Residual Plot of " + y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands)
                fig = plt.gcf()
                fig.set_size_inches(16,9)
                fig.tight_layout()
                fig.savefig("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\Line Fit - Bigger Font\\" + y_Axis + " vs\\" + y_Axis +
                            " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands + " Residual Plot.pdf")
                #plt.show(block=False)
                #plt.pause(5)
                plt.close("all")
                count += 1
                print(count/total)
