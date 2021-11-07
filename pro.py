from os import read
import pandas as pd
import statistics
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv(r"StudentsPerformance.csv")

mathscore=df["math score"].tolist()

mean=statistics.mean(mathscore)
median=statistics.median(mathscore)
mode=statistics.mode(mathscore)
sd=statistics.stdev(mathscore)

print(mean,median,mode,sd)

sd_1_start,sd_1_end=mean-sd,mean+sd
sd_2_start,sd_2_end=mean-(2*sd),mean+(2*sd)
sd_3_start,sd_3_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([mathscore],["scores"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[sd_1_start,sd_1_start],y=[0,1],mode="lines",name="STD DEV 1"))
fig.add_trace(go.Scatter(x=[sd_1_end,sd_1_end],y=[0,1],mode="lines",name="STD DEV 1"))

fig.add_trace(go.Scatter(x=[sd_2_start,sd_2_start],y=[0,1],mode="lines",name="STD DEV 2"))
fig.add_trace(go.Scatter(x=[sd_2_end,sd_2_end],y=[0,1],mode="lines",name="STD DEV 2"))

fig.show()

list_of_data_within_1SD=[result for result in mathscore if result>sd_1_start and result<sd_1_end]
list_of_data_within_2SD=[result for result in mathscore if result>sd_2_start and result<sd_2_end]
list_of_data_within_3SD=[result for result in mathscore if result>sd_3_start and result<sd_3_end]

print("{}% of data lying within 1SD ".format(len(list_of_data_within_1SD)*100/len(mathscore)))
print("{}% of data lying within 2SD ".format(len(list_of_data_within_2SD)*100/len(mathscore)))
print("{}% of data lying within 3SD ".format(len(list_of_data_within_3SD)*100/len(mathscore)))