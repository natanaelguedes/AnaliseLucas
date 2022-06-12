

import plotly.graph_objects as go

categories = ['Comunidade participa ','Abaixo assinados',' Ocupação','Solicitação comunitária']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [5.0,3.0, 2.0,2.0],
      theta=categories,
      fill='toself',
      name='Participação nas tomadas de decisões coletivas'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True
)

fig.show()