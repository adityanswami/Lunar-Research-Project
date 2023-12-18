from pypdf import PdfMerger

file = open("R greater than 0.7.txt", 'r')
lines = file.readlines()
names = []

for i in range(len(lines)):
    if i != 0 and i != 1:
        names.append(lines[i].split('\t')[0])
pdfs = []
merger = PdfMerger()
print(names[0])
for name in names:
    print(name)
    y_axis = name.split(' ')[0] + " " + name.split(' ')[1] + " " + name.split(' ')[2] + " " + name.split(' ')[3]
    othery = name.split(' ')[1] + " " + name.split(' ')[2] + " " + name.split(' ')[3]
    rename = name.split(' ')[1] + " " + name.split(' ')[2] + " " + name.split(' ')[3] + " " + name.split(' ')[5] + " " + name.split(' ')[6] + " " + name.split(' ')[7] + " " + name.split(' ')[8] + " " + name.split(' ')[9]
    pdfs.append("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\Line Fits of Standardized Datapoints\\" + y_axis + "\\" + name + ".pdf")
    pdfs.append("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\Line Fits of Standardized Datapoints\\" + y_axis + "\\" + name + " Residual Plot.pdf")
    pdfs.append("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\Line Fit\\" + othery + "\\" + rename + ".pdf")
    pdfs.append("C:\\Users\\adity\\School\\ExMASS\\Data Analysis\\Graphs\\Line Fit\\" + othery + "\\" + rename + " Residual Plot.pdf")
for i in range(len(pdfs)):
    merger.append(pdfs[i])
merger.write("All Aprroximately Linear Graphs.pdf")
merger.close()
file.close()