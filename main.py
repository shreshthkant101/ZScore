import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics as st
import plotly.graph_objects as gob
import random as r


fileData = pd.read_csv("data.csv")["Math_score"].tolist()

figure = ff.create_distplot([fileData],["Math Scores"],show_hist=False)
figure.show()

mean = st.mean(fileData)

std = st.stdev(fileData)

print(mean)

print(std)