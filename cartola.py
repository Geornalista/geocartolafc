import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


times = ['América-MG','Athlético-PR','Atlético-GO','Atlético-MG','Bahia','Bragantino','Ceará',
        'Chapecoense','Corinthians','Cuiabá','Flamengo','Fluminense','Fortaleza','Grêmio',
        'Internacional','Juventude','Palmeiras','Santos','Sport','São Paulo']

posicoes = ['Goleiro','Zagueiro','Lateral','Meia','Atacante']

rodada_atual = 28

rods = []
for i in range(rodada_atual):
  rods.append(i+1)

st.sidebar.write(
    """
    **CARTOLAFC **

    """
)

st.sidebar.header('Escolha os times')

dropdown1 = st.sidebar.selectbox('Escolha os times', times)
radio = st.sidebar.radio('Escolha uma posição:',posicoes)

filename = 'cartola.xlsx'
cartola = pd.read_excel(filename, engine= 'openpyxl')
cartola.drop('Unnamed: 0',axis=1,inplace=True)

if len(dropdown1) > 0:

  df = cartola.query('TIME == "{}" & POSICAO == "{}"'.format(dropdown1,radio))

  df.rename({'G':'GOLS','A':'ASSISTÊNCIA','FT':'FINALIZAÇÃO NA TRAVE',
          'SG':'JOGO SEM SOFRER GOL','DP':'DEFESA DE PÊNALTI',
          'DE':'DEFESA','DS':'DESARME','GC':'GOL CONTRA',
          'CV':'CARTÃO VERMELHO','CA':'CARTÃO AMARELO',
          'GS':'GOL SOFRIDO','FC':'FALTA COMETIDA',
          'PC':'PÊNALTI COMETIDO','FD':'FINALIZAÇÃO DEFENDIDA',
          'FF':'FINALIZAÇÃO PRA FORA','FS':'FALTA SOFRIDA',
          'PP':'PÊNALTI PERDIDO','I':'IMPEDIMENTO',
          'PI':'PASSE INCOMPLETO','PS':'PÊNALTI SOFRIDO',
          }, axis=1, inplace=True)
  
  teste = st.checkbox('Selecionar Jogador')
  
  if teste:
    jogadores = df['NOME'].unique()
    dropdown2 = st.selectbox('Escolha o Jogador', jogadores)

    if len(dropdown2) > 0:

      df1 = df.query('NOME == "{}"'.format(dropdown2))

      scouts1 = list(df.columns)
      remove = ['TIME','POSICAO','NOME','RODADA','ADVERSARIO','CASA','FORA']
      scouts=[]
      for item in scouts1:
        if item not in remove:
          scouts.append(item)

      dropdown3 = st.selectbox('Escolha o scout', scouts)
      
      pontos=[]
      for rod in range(rodada_atual):
        pontos.append(df1[df1['RODADA']==rod+1][dropdown3].sum())

      df2 = pd.DataFrame(
              {'RODADA':rods,
               dropdown3:pontos
               })

      st.header('Time: {} - Posição: {} - Jogador: {}'.format(dropdown1,radio,dropdown2))
      st.write('TOTAL DE {}'.format(dropdown3))

      bar = alt.Chart(df2, height=400, width=900).mark_bar(size=20).encode(
        x='RODADA',
        y=dropdown3,
        color=alt.value('darkgreen')
        ).configure_axis(
          labelFontSize=20,
          titleFontSize=20
        )

      st.altair_chart(bar)
