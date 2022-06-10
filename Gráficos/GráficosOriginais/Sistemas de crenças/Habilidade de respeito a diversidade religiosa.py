import angles
import ax as ax
import plotly.graph_objects as go
from matplotlib import pyplot as plt


classes = ['Respeito','Idosos','Recreação','Forró','MLI – Movimento de Luta dos Idosos','Projeto Raízes da Favela','Atendimento Psicológico','Bingo']


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[3,2, 2, 2,2,2,1,1],
      theta=classes,
      fill='toself',
      name='Manutenção de saberes locais'
))
fig.show()