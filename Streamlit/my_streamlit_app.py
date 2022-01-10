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
df = df_voiture
df_Japan = df_voiture[df_voiture['continent'] == ' Japan.']
df_US = df_voiture[df_voiture['continent'] == ' US.']
df_EU = df_voiture[df_voiture['continent'] == ' Europe.']



col1, col2, col3= st.columns([3,3,3])

with col2:
    all_button = st.button("Toutes les régions.")
    if all_button:
        df = df_voiture


col1, col2, col3= st.columns([3,3,3])


with col1:
    US_button = st.button("US")
    if US_button:
        df = df_US

with col2:
    EU_button = st.button("Europe")
    if EU_button:
        df = df_EU

with col3:
    Japan_button = st.button("Japon")
    if Japan_button:
        df = df_Japan

df

corr = df.corr()
fig = go.Figure()
fig.add_trace(go.Heatmap(
    z = corr,
    x = corr.columns.values,
    y = corr.columns.values,
    colorscale = px.colors.diverging.RdBu,
    zmid=0
))

fig.update_layout(width=1000, height=900)
st.plotly_chart(fig)

st.write("Comme le montre bien la heatmap. La catégorie 'mpg' est fortement corrélée aux catégories 'cylinders', 'cubicinches', 'hp', 'weightlbs'. On constate également que la catégorie 'hp' est corrélée à la catégorie 'time_to_60'.")