from math import sqrt
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics as st
import plotly.graph_objects as gob
import random as r
 

fileData = pd.read_csv("data.csv")["Math_score"].tolist()

totalmean = st.mean(fileData)

totalArray = []
def sample(index, total): 
    if index < 3:

        dataSet = []
        for i in range(0,100):
            item = fileData[r.randint(0,len(fileData) - 1)]

            dataSet.append(item)

        total.append(dataSet)
        index += 1
        sample(index,total)
     

sample(0,totalArray)

means = []
for i in totalArray:
    means.append(st.mean(i))
 
ourmean = means[0]

ar = totalArray[0]


stdev = st.stdev(ar) / sqrt(100)
 

#firststandarddeviation

firststandarddeviationstart , firststandarddeviationend  = ourmean - stdev , ourmean + stdev

#secondstandarddeviation
secondstandarddeviationstart , secondstandarddeviationend = ourmean - stdev * 2 , ourmean + stdev * 2

#thirdstandarddeviation

thirdstandarddeviationstart, thirdstandarddeviationend = ourmean - stdev * 3, ourmean + stdev * 3

zscore = (ourmean - totalmean) / stdev

print(zscore)