

import plotly.graph_objects as go

categories = ['Respeito','Idoso','Recreação','Forró','MLI-Movimento de Luta dos idosos','Projeto Raizes da Favela','Atendimento Psicológico','Bingo']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [4.0, 3.0, 2.0,2.0,2.0,2.0,1.0,1.0],
      theta=categories,
      fill='toself',
      name='Respeito a Ancianidade'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 4]
    )),
  showlegend=False
)

fig.show()