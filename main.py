import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard de vacinações dos países")

df = pd.read_csv('vacinacao_corrigido.csv')

df['date'] = pd.to_datetime(df['date'])

fig1 = px.line(df, x='date', y = 'total_vaccinations', color='location',
               title = "Total de vacinações por Data e Países" )
fig1.update_layout(xaxis_title='Date', yaxis_title='Total de vacinações')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

df_filtro = df.query('location == "BRAZIL" or location == "INDIA" or location == "UNITED STATES"')

fig2 = px.pie(df_filtro, names='location', values='people_fully_vaccinated',
              title= 'Pessoas totalmente vacinadas do Brasil, India e Estados Unidos')
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
