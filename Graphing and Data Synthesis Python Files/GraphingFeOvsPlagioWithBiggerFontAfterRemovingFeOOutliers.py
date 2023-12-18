import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
import seaborn
import time
import numpy
import scipy

plt.rcParams.update({"font.size": 25})
crater_types = ["All"]
mHBoth = ["maria", "highlands", "both"]
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
                df = pd.read_excel("All Crater Data Removing FeO Outliers.xlsx")
                colors = seaborn.color_palette(n_colors=len(set(df["Crater ID"])))
                colors_dict = dict((k, v) for k, v in enumerate(colors))
                crater_id_dict = pd.DataFrame(set(df["Crater ID"]))[0].to_dict()
                crater_id_dict = dict((v, k) for k, v in crater_id_dict.items())
                x = df[x_Axis]
                y = df[y_Axis]
                z = df["Crater ID"]
                numbered_crater_id = df["Crater ID"].map(crater_id_dict)
                if mariaOrHighlands == "maria":
                    plt.scatter(df.loc[df["Highlands?"] == "maria"][x_Axis],
                                df.loc[df["Highlands?"] == "maria"][y_Axis],
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["maria"], facecolors="None", label="Datapoints from Maria Craters")
                    x = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    y_pred = intercept + slope * x
                    label = "LSRL: slope = " + str(round(slope, 3)) + ", intercept = " + str(round(intercept, 3)) + ", r = " + str(round(rvalue, 3))
                    plt.plot(x,y_pred, color="black", label=label)
                elif mariaOrHighlands == "highlands":
                    plt.scatter(df.loc[df["Highlands?"] == "highlands"][x_Axis],
                                df.loc[df["Highlands?"] == "highlands"][y_Axis],
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["highlands"], facecolors="None", label="Datapoints from Highlands Craters")
                    x = numpy.array(df.loc[df["Highlands?"] == "highlands"][x_Axis])
                    y = numpy.array(df.loc[df["Highlands?"] == "highlands"][y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    y_pred = intercept + slope * x
                    label = "LSRL: slope = " + str(round(slope, 3)) + ", intercept = " + str(round(intercept, 3)) + ", r = " + str(round(rvalue, 3))
                    plt.plot(x, y_pred, color="black", label=label)
                else:
                    plt.scatter(df.loc[df["Highlands?"] == "highlands"][x_Axis],
                                df.loc[df["Highlands?"] == "highlands"][y_Axis],
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["highlands"], facecolors="None", label="Datapoints from Highlands Craters")
                    plt.scatter(df.loc[df["Highlands?"] == "maria"][x_Axis],
                                df.loc[df["Highlands?"] == "maria"][y_Axis],
                                edgecolors=numbered_crater_id.map(colors_dict),
                                marker=markers["maria"], facecolors="None", label="Datapoints from Maria Craters")
                    x = numpy.array(df[x_Axis])
                    y = numpy.array(df[y_Axis])
                    mask = ~numpy.isnan(x) & ~numpy.isnan(y)
                    (slope, intercept, rvalue, pvalue, stderr) = scipy.stats.linregress(x[mask], y[mask])
                    y_pred = intercept + slope * x
                    label = "LSRL: slope = " + str(round(slope, 3)) + ", intercept = " + str(round(intercept, 3)) + ", r = " + str(round(rvalue, 3))
                    plt.plot(x, y_pred, color="black", label=label)
                plt.legend(loc="best")
                plt.xlabel(x_Axis)
                plt.ylabel(y_Axis)
                plt.title(y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands)
                fig = plt.gcf()
                fig.set_size_inches(16,9)
                fig.tight_layout()
                fig.savefig("C:\\Users\\adity\\ExMASS\\Data Analysis\\Graphs\\Line Fit - Bigger Font\\" + y_Axis + " vs\\" + y_Axis + " Outliers Removed\\" + y_Axis +
                            " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands + ".pdf")
                #plt.show(block=False)
                #plt.pause(5)
                plt.close("all")
                count += 1
                print(count/total)

