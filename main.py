import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
score=df["math score"].tolist()
mean=st.mean(score)
median=st.median(score)
mode=st.mode(score)
sd=st.stdev(score)
print(mean,median,mode,sd)
sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(3*sd),mean+(3*sd)
fig=ff.create+distplot([score],["score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.1],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.1],mode-"lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.1],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.1],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.1],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.1],mode="lines",name="sd3"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.1],mode="lines",name="sd3"))
listofdatawithin1sd=[result for result in score if result>sd1start and result<sd1end]
listofdatawithin1sd=[result for result in score if result>sd2start and result<sd2end]
listofdatawithin1sd=[result for result in score if result>sd3start and result<sd3end]
print("{}%of data lies within 1sd".format(len(listofdatawithin1sd)*100.0/len(score)))
print("{}%of data lies within 2sd".format(len(listofdatawithin2sd)*100.0/len(score)))
print("{}%of data lies within 3sd".format(len(listofdatawithin3sd)*100.0/len(score)))
fig.show()      