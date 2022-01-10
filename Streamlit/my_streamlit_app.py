import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Données voitures', page_icon='👈', layout="wide")

st.markdown("<h1 style='text-align: center;'>Streamlit : build and share data apps</h1>", unsafe_allow_html=True)


col1, col2, col3= st.columns([3,8,3])
col2.image('Streamlit/assets/challenge.png', use_column_width=True)

df_voiture = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
df = df_voiture
df_Japan = df_voiture[df_voiture['continent'] == ' Japan.']
df_US = df_voiture[df_voiture['continent'] == ' US.']
df_EU = df_voiture[df_voiture['continent'] == ' Europe.']

#VIZ
config = {'displayModeBar': False} # improve visualisation




st.markdown('* mpg : consommation en miles par gallon (impérial)')
st.markdown('* cylinders : nombre de cylindres de la voiture')
st.markdown('* cubinches : cylindrée en cubic inches (122 cubic inches = 2 litres)')
st.markdown('* hp : puissance en chevaux')
st.markdown('* weightlbs : poids en livres (1 livre = 0.454 kg')
st.markdown('* time-to-60 : temps pour aller de 0 à 60 miles par heure (presque équivalent au 0 à 100 kmh)')
st.markdown('* year : année de sortie du modèle')
st.markdown('* continent : région d\'origine de la voiture (entre Europe, USA et Japon)')


col1, col2, col3= st.columns([3,3,3])

with col2:
    all_button = st.button("Toutes les régions")
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

col1, col2, col3= st.columns([1,8,1])

with col2:
    df


st.write("Aperçu des données proposées dans la heatmap ci-dessous.")
col1, col2, col3= st.columns([1,8,1])

with col2:

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
    st.plotly_chart(fig, config = config, use_container_width = True)

st.write("Comme le montre la heatmap quand on sélectionne toutes les régions. La catégorie 'mpg' est fortement corrélée aux catégories 'cylinders', 'cubicinches', 'hp', 'weightlbs'. On constate également que la catégorie 'hp' est corrélée à la catégorie 'time_to_60'. C'est également vrai quand on sélectionné la région 'US' mais les données sont assez différentes sur la région 'Japon' et 'Europe'.")


st.markdown("<h1 style='text-align: center;'>Voitures produites par région</h1>", unsafe_allow_html=True)


count_list = {'Region': ['US', 'Europe', 'Japon'], 'Nombre de voitures': [len(df_US.index), len(df_EU.index), len(df_Japan.index)]}
df_count = pd.DataFrame(count_list)  

col1, col2, col3= st.columns([1,8,1])

with col2:

    fig = px.bar(df_count, x="Region", y="Nombre de voitures")
    st.plotly_chart(fig, config = config, use_container_width = True)

st.write("Il y a bien plus de voitures produites aux US qu'en Europe et au Japon.")



col1, col2, col3= st.columns([3,3,3])

with col1:
    fig = px.histogram(df_US, x="year")
    st.plotly_chart(fig, config = config, use_container_width = True)


with col2:
    fig = px.histogram(df_EU, x="year")
    st.plotly_chart(fig, config = config, use_container_width = True)

with col3:
    fig = px.histogram(df_Japan, x="year")
    st.plotly_chart(fig, config = config, use_container_width = True)






