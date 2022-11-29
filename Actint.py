import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import integer
import matplotlib.pyplot as plt
import missingno as msno
from datetime import date,time,datetime,timedelta
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly as px
import plotly
import seaborn as sns



st.title('Police Department Incident Reports from 2018 to 2020')

df=pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

#Mapa Incidentes
st.subheader('Total Incidents Map')
st.write('In this following map we can see the location of each of the reports generated in these 3 years of registration, so we can analyze which are the most dangerous areas in San Francisco.')
mapa = df[['Latitude','Longitude']]
mapa=mapa.rename(columns={"Latitude": "lat", "Longitude": "lon"})
mapa = mapa.dropna()
st.map(data= mapa, zoom=11,  use_container_width=True)



st.subheader('Original data frame with all records')
st.write('This table contains all the records with which the analysis of the police department will be carried out.')
st.dataframe(df)
#Quitar Columnas sin descripcion 
df1 = df
df1 = df1.dropna(subset=["Analysis Neighborhoods"])
df1 = df1.drop(['HSOC Zones as of 2018-06-05', 'OWED Public Spaces', 'Central Market/Tenderloin Boundary Polygon - Updated','Parks Alliance CPSI (27+TL sites)','ESNCAG - Boundary File'], axis=1)


#Dataframe Limpio y por Año


df18 = df1[(df1['Incident Year'] == 2018)]
df19 = df1[(df1['Incident Year'] == 2019)]
df20 = df1[(df1['Incident Year'] == 2020)]


#Tablas Plotly
st.subheader('Table of Reports by Year')
st.write('For a first analysis we must observe the behavior of the number of reports per year in this city to see what is the trend it is facing, so this table is one of the most important to show results in the medium term.')
freq = df1.groupby('Incident Year')[['Analysis Neighborhoods']].count() 
fig = go.Figure()

fig.add_trace(go.Pie(labels=freq.index, values=freq['Analysis Neighborhoods']))
fig.update_layout(
xaxis_title="Days",
yaxis_title="Total",
legend_title="Variables",
font=dict(
     family="Timesnewroman, monospace",
     size=18,
     color="white"))

st.plotly_chart(fig, use_container_width=True)

#Seleccion de Opcines 

st.subheader('View by Year')
st.write('In the following menu you can select the year you want to view, where a map will be displayed with the location of the reports for the selected year and three other graphs with analyzes that will be specified later.')

op = st.selectbox('Select the Year',('2018', '2019', '2020'))

st.write('You selected:', op)
if op == '2018':
    st.subheader('Incident Map 2018')
    mapa18 = df18[['Latitude','Longitude']]
    mapa18 =mapa18.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa18 = mapa18.dropna()
    st.map(mapa18)
    
    freq2 = df18.groupby('Analysis Neighborhoods')[['Analysis Neighborhoods']].count() 
    names = df18['Analysis Neighborhood'].unique()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=names, y=freq2['Analysis Neighborhoods'],marker_color='rgb(158,202,225)'))
    fig2.update_layout(
        title="Neighborhood and number of reports",
        xaxis_title="Neighborhoods",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=10,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig2, use_container_width=True)
    st.write('The table above shows which neighborhoods have the most reports to the police, counting in the thousands in the year-round record.')

    freq4 = df18.groupby('Incident Category')[['Incident Category']].count()
    fig4 = go.Figure()

    fig4.add_trace(go.Bar(x=freq4.index, y=freq4['Incident Category']))
    fig4.update_layout(
        title="Number of Reports by Category",
        xaxis_title="Report",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=8,
        yaxis_tickfont_size=10,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig4, use_container_width=True)
    st.write('This graph shows which are the most common crimes recorded throughout the year, with robbery being the most common category on this list but which is divided into many other subcategories.')
    
    
    
if op == '2019':
    st.subheader('Incident Map 2019')
    mapa19 = df19[['Latitude','Longitude']]
    mapa19 =mapa19.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa19 = mapa19.dropna()
    st.map(mapa19)

    freq2 = df19.groupby('Analysis Neighborhoods')[['Analysis Neighborhoods']].count() 
    names = df19['Analysis Neighborhood'].unique()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=names, y=freq2['Analysis Neighborhoods'],marker_color='rgb(158,202,225)'))
    fig2.update_layout(
        title="Neighborhood and number of reports",
        xaxis_title="Neighborhoods",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=10,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig2, use_container_width=True)
    st.write('The table above shows which neighborhoods have the most reports to the police, counting in the thousands in the year-round record.')
    freq4 = df19.groupby('Incident Category')[['Incident Category']].count()
    fig4 = go.Figure()

    fig4.add_trace(go.Bar(x=freq4.index, y=freq4['Incident Category']))
    fig4.update_layout(
        title="Number of Reports by Category",
        xaxis_title="Reporte",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=8,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig4, use_container_width=True)
    st.write('This graph shows which are the most common crimes recorded throughout the year, with robbery being the most common category on this list but which is divided into many other subcategories.')
    
    
    
    
    
if op == '2020':
    st.subheader('Incident Map 2020')
    mapa20 = df20[['Latitude','Longitude']]
    mapa20 =mapa20.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa20 = mapa20.dropna()
    st.map(mapa20)

    freq2 = df20.groupby('Analysis Neighborhoods')[['Analysis Neighborhoods']].count()
    names = df20['Analysis Neighborhood'].unique()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=names, y=freq2['Analysis Neighborhoods'],marker_color='rgb(158,202,225)'))
    fig2.update_layout(
        title="Neighborhood and number of reports",
        xaxis_title="Neighborhoods",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=10,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig2, use_container_width=False)
    st.write('The table above shows which neighborhoods have the most reports to the police, counting in the thousands in the year-round record.')



    
    freq4 = df20.groupby('Incident Category')[['Incident Category']].count() 
    
    fig4 = go.Figure()

    fig4.add_trace(go.Bar(x=freq4.index, y=freq4['Incident Category']))
    fig4.update_layout(
        title="Number of Reports by Category",
        xaxis_title="Reporte",
        yaxis_title="Total",
        legend_title="Variables",
        xaxis_tickfont_size=8,
    font=dict(
        family="Timesnewroman, monospace",
        size=18,
        color="white"))
    st.plotly_chart(fig4, use_container_width=True)
    st.write('This graph shows which are the most common crimes recorded throughout the year, with robbery being the most common category on this list but which is divided into many other subcategories.')
    


st.subheader('Days with more number of reports')
freq3 = df1.groupby('Incident Day of Week')[['Analysis Neighborhoods']].count() 
fig3 = go.Figure()

fig3.add_trace(go.Bar(x=freq3.index, y=freq3['Analysis Neighborhoods'],base = df['Analysis Neighborhoods'].unique(),marker_color='rgb(158,50,225)'))
fig3.update_layout(
     xaxis_title="Days",
     yaxis_title="Total",
     legend_title="Variables",
 font=dict(
     family="Timesnewroman, monospace",
     size=18,
     color="white"))
st.plotly_chart(fig3, use_container_width=True)

st.write('In this additional table, the expectation is related to observe the behavior of the reports throughout the week, this is how we can observe that if there is a difference but it is not entirely significant, it indicates that there is a day that is with the highest crime rate.') 





st.subheader('Report status')
freq4 = df1.groupby('Resolution')[['Resolution']].count() 
fig4 = go.Figure()

fig4.add_trace(go.Bar(x=freq4.index, y=freq4['Resolution'],marker_color='rgb(158,50,225)'))
fig4.update_layout(
     xaxis_title="Statuss",
     yaxis_title="Total",
     legend_title="Variables",
 font=dict(
     family="Timesnewroman, monospace",
     size=18,
     color="white"))
st.plotly_chart(fig4, use_container_width=True)
st.write('In this graph you can see the status of the total cases throughout these three years, where it can be seen that the majority of cases are still open and the others have reached a solution') 
