

import plotly.graph_objects as go

categories = ['Faltam projetos coletivos ','Horta coletiva',' Projeto de psicultura']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [9.0, 2.0,1.0],
      theta=categories,
      fill='toself',
      name='Participação coletiva comunitária na gestão de negócios'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 9]
    )),
  showlegend=True
)

fig.show()