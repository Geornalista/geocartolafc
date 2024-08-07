import streamlit as st
import pandas as pd
import plotly.graph_objs as go

times = ['Athlético-PR','Atlético-GO','Atlético-MG','Bahia','Botafogo',
        'Bragantino','Corinthians','Criciúma','Cruzeiro','Cuiabá','Flamengo',
        'Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Palmeiras',
        'São Paulo','Vasco','Vitória']

posicoes = ['Goleiro','Lateral','Zagueiro','Meia','Atacante','Técnico']

st.sidebar.header('Escolha o time')
dropdown1 = st.sidebar.selectbox('Escolha o time', times)

st.sidebar.header('Escolha a posição')
radio = st.sidebar.radio('Escolha uma posição:',posicoes)

filename = 'cartola.csv'
cartola = pd.read_csv(filename)
cartola.drop('Unnamed: 0',axis=1, inplace=True)

rod = cartola['RODADA'].max()
st.header(f'RODADA ATUAL: {rod}')

if len(dropdown1) > 0:

  df = cartola.query('ADVERSARIO == "{}" & POSICAO == "{}"'.format(dropdown1,radio))
  df1 = df[['NOME', 'PONTUACAO']]
  df1.sort_values(by='PONTUACAO',inplace=True)
  hh = df1.shape[0]
  if hh > 30:
    hheight = 1200
  else:
    hheight = 600

  fig = go.Figure(
        data=[go.Bar(x = df1['PONTUACAO'], y = df1['NOME'],
          name='PONTUACAO',orientation='h',marker_color='darkgreen')])

  fig.update_layout(
    xaxis_title="Pontos",
    autosize=True,
    width=1000,
    #height=hheight,
    height=600,
    margin=dict(
        l=50,
        r=10,
        b=10,
        t=50,
        pad=0.1
    ),

    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        zeroline=True,
    ),
    font=dict(family="Arial",size=24,color="Red"),
    paper_bgcolor="white",
    plot_bgcolor="silver",
    )

  st.header('{}: Pontuação enfrentando {}'.format(radio,dropdown1))

  st.plotly_chart(fig)
