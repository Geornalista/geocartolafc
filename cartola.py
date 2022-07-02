import streamlit as st
#import altair as alt
import pandas as pd
import plotly.graph_objs as go

times = ['América-MG','Athlético-PR','Atlético-GO','Atlético-MG','Avaí','Botafogo',
        'Bragantino','Ceará','Corinthians','Coritiba','Cuiabá','Flamengo',
        'Fluminense','Fortaleza','Goiás','Internacional','Juventude',
        'Palmeiras','Santos','São Paulo']

posicoes = ['Goleiro','Lateral','Zagueiro','Meia','Atacante','Técnico']

st.sidebar.write(
    """
    **CARTOLAFC 2022 **

    """
)

st.sidebar.header('Escolha os times')

dropdown1 = st.sidebar.selectbox('Escolha os times', times)
radio = st.sidebar.radio('Escolha uma posição:',posicoes)

filename = 'cartola.csv'
cartola = pd.read_csv(filename)
cartola.drop('Unnamed: 0',axis=1, inplace=True)

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
          name='PONTUACAO',orientation='h',marker_color='green')])

  fig.update_layout(
    xaxis_title="Pontos",
    autosize=False,
    width=850,
    height=hheight,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
        pad=2
    ),

    yaxis=dict(
        showgrid=True,
        showline=False,
        showticklabels=True,
        zeroline=True,
    ),
    paper_bgcolor="white",
    plot_bgcolor="darkgray",
    )

  st.header('{}: Pontuação enfrentando {}'.format(radio,dropdown1))

  st.plotly_chart(fig)
