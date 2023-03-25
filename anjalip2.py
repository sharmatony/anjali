# -*- coding: utf-8 -*-
"""anjalip2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qcRY7Q2TwNJ2qI7T-S94GlNx116g8_em
"""

from google.colab import drive
drive.mount('/content/drive')

#import library
import pandas as pd
import plotly.express as pr
import plotly.graph_objects as go

df = pd.read_csv('/content/project_dataset.csv ')

df

df.shape

dfl = df.copy()

dfl.head(50)

dfl.columns

dfl.info()

dfl.describe()



dfl.isna()

dfl.isna().sum()

dfl.isna().sum()/dfl.shape[0]

dfl.dropna(axis = 1 , inplace=True)

dfl.dtypes

dfl.shape

data=dfl.sample(n=500,random_state = 40)

data

data.shape

data.head

data.tail

data.count()

data = data.drop(['Unnamed: 0'], axis=1)

data

data.shape

data

fig = go.Figure(data=go.Scatter(x=df['Distance'], y=df['DepTime'],mode='markers',marker=dict(color='red')))

fig.update_layout(title='Scatter plot for distance vs departure time',xaxis_title ='distance',yaxis_title='departure time')
fig.show()

line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
line_data

fig = go.Figure(data=go.Scatter(x=line_data['Month'],y=line_data['ArrDelay'],mode='lines',marker=dict(color='green')))
fig.update_layout(title='Month vs Arrival Delay in timeplot',xaxis_title='Month',yaxis_title='Delay of flight Arrival(in minutes)')
fig.show()

bar_data = df.groupby(['DestState'])['Flights'].sum().reset_index()
bar_data

fig = pr.bar(bar_data, x="DestState",y="Flights",title='Total number of flight from  the destnation states')
fig.show()

bub_data = df.groupby('Reporting_Airline')['Flights'].sum().reset_index()

bub_data

fig = pr.bar(bar_data, x = 'DestState', y='Flights', title = 'Total number of flights from each destination states')
fig.show()

