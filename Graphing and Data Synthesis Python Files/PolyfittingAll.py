import sys

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
import seaborn
import time
import numpy
import scipy


degs = [1]

crater_types = ["C", "A", "D", "All"]
mHBoth = ["maria", "highlands", "both"]
x_Axes_List = ["Standardized Position", "Position", "Longitude", "Latitude", "Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight",
               "Iron Abundance", "Olivine Abundance", "Orthopyroxene Abundance", "Plagioclase Abundance",
               "TerrainSlope", "Titanium Abundance"]
y_Axes_List = ["Clinopyroxene Abundance", "FeO Abundance", "TerrainHeight", "Iron Abundance", "Olivine Abundance",
               "Orthopyroxene Abundance", "Plagioclase Abundance", "TerrainSlope", "Titanium Abundance"]
count = 0
total = len(crater_types)*len(mHBoth)*len(x_Axes_List)*len(y_Axes_List)*len(degs)
markers = {
    "maria": ".",
    "highlands": "^"
}
for deg in degs:
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
                        plt.scatter(df.loc[df["Highlands?"] == "maria"][x_Axis],
                                    df.loc[df["Highlands?"] == "maria"][y_Axis],
                                    edgecolors=numbered_crater_id.map(colors_dict),
                                    marker=markers["maria"], facecolors="None", label="Datapoints from Maria Craters")
                        x = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                        y = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])
                        idx = numpy.isfinite(x) & numpy.isfinite(y)
                        xs = x[idx].tolist()
                        ys = y[idx].tolist()
                        if len(xs) != 0 and len(ys) != 0:
                            coeffs, SSE, rubbish1, rubbish2, rubbish3 = numpy.polyfit(x[idx],y[idx], deg, full=True)
                            error_from_mean = []
                            for element in y:
                                if numpy.isnan(element) == False:
                                    error_from_mean.append(element - numpy.nanmean(y))
                            SST = sum(error_from_mean)
                            r_square = 1-(SSE/SST)
                            eqn = r'$'
                            preds = []
                            x = x.tolist()
                            x.sort()
                            for element in x:
                                y_pred = 0
                                for coeff_index in range(len(coeffs)):
                                    y_pred = y_pred + (coeffs[coeff_index]) * (element ** coeff_index)
                                preds.append(y_pred)
                            for coeff_index in range(len(coeffs)):

                                eqn = eqn + str(coeffs[coeff_index])
                                if coeff_index == 0:
                                    eqn = eqn + "+"
                                elif coeff_index != deg:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}+"
                                else:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}"
                            eqn += '$'
                            label = r"Polynomial fit: " + eqn + ", R^2 = " + str(r_square)

                            plt.plot(x,preds, color="black", label=label)
                    elif mariaOrHighlands == "highlands":
                        plt.scatter(df.loc[df["Highlands?"] == "highlands"][x_Axis],
                                    df.loc[df["Highlands?"] == "highlands"][y_Axis],
                                    edgecolors=numbered_crater_id.map(colors_dict),
                                    marker=markers["highlands"], facecolors="None", label="Datapoints from Highlands Craters")
                        x = numpy.array(df.loc[df["Highlands?"] == "maria"][x_Axis])
                        y = numpy.array(df.loc[df["Highlands?"] == "maria"][y_Axis])
                        idx = numpy.isfinite(x) & numpy.isfinite(y)
                        xs = x[idx].tolist()
                        ys = y[idx].tolist()
                        if len(xs) != 0 and len(ys) != 0:
                            coeffs, SSE, rubbish1, rubbish2, rubbish3 = numpy.polyfit(x[idx], y[idx], deg, full=True)
                            error_from_mean = []

                            for element in y:
                                if numpy.isnan(element) == False:
                                    error_from_mean.append(element - numpy.nanmean(y))
                            SST = sum(error_from_mean)
                            r_square = 1 - (SSE / SST)
                            eqn = r'$'
                            preds = []
                            x = x.tolist()
                            x.sort()
                            for element in x:
                                y_pred = 0
                                for coeff_index in range(len(coeffs)):
                                    y_pred = y_pred + (coeffs[coeff_index]) * (element ** coeff_index)
                                preds.append(y_pred)
                            for coeff_index in range(len(coeffs)):

                                eqn = eqn + str(coeffs[coeff_index])
                                if coeff_index == 0:
                                    eqn = eqn + "+"
                                elif coeff_index != deg:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}+"
                                else:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}"
                            eqn += '$'
                            label = r"Polynomial fit: " + eqn + ", R^2 = " + str(r_square)

                            plt.plot(x, preds, color="black", label=label)
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
                        idx = numpy.isfinite(x) & numpy.isfinite(y)
                        xs = x[idx].tolist()
                        ys = y[idx].tolist()
                        if len(xs) != 0 and len(ys) != 0:
                            coeffs, SSE, rubbish1, rubbish2, rubbish3 = numpy.polyfit(x[idx], y[idx], deg, full=True)
                            error_from_mean = []
                            for element in y:
                                if numpy.isnan(element) == False:
                                    error_from_mean.append(element - numpy.nanmean(y))
                            SST = sum(error_from_mean)
                            r_square = 1 - (SSE / SST)
                            eqn = r'$'
                            preds = []
                            x = x.tolist()
                            x.sort()
                            for element in x:
                                y_pred = 0
                                for coeff_index in range(len(coeffs)):
                                    y_pred = y_pred + (coeffs[coeff_index]) * (element ** coeff_index)
                                preds.append(y_pred)
                            for coeff_index in range(len(coeffs)):

                                eqn = eqn + str(coeffs[coeff_index])
                                if coeff_index == 0:
                                    eqn = eqn + "+"
                                elif coeff_index != deg:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}+"
                                else:
                                    eqn = eqn + "x^{" + str(coeff_index) + "}"
                            eqn += '$'
                            label = r"Polynomial fit: " + eqn + ", R^2 = " + str(r_square)

                            plt.plot(x, preds, color="black", label=label)

                    if len(xs) != 0 and len(ys) != 0:
                        plt.legend(loc="best")
                        plt.xlabel(x_Axis)
                        plt.ylabel(y_Axis)
                        plt.title(y_Axis + " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands)
                        fig = plt.gcf()
                        fig.set_size_inches(16,9)
                        fig.tight_layout()
                        fig.savefig("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\" + str(deg) + " Degree Polynomial Fits\\" + y_Axis + " vs\\" + y_Axis +
                                    " vs " + x_Axis + " " + which_craters + " Craters " + mariaOrHighlands + ".pdf")
                        #plt.show(block=False)
                        #plt.pause(5)
                        plt.close("all")
                        count += 1
                        print(count/total)

