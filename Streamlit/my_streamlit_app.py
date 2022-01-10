import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Streamlit : build and share data apps")
st.image('Streamlit/assets/challenge.png')

df_voiture = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')




corr = df_voiture.corr()
fig = go.Figure()
fig.add_trace(go.Heatmap(
    z = corr,
    x = corr.columns.values,
    y = corr.columns.values,
    colorscale = px.colors.diverging.RdBu,
    zmid=0
))

fig.update_layout(width=1000, height=900)
st.plotly_chart(fig.show())