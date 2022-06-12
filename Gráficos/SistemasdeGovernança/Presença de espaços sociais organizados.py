

import plotly.graph_objects as go

categories = ['Projeto Uma Mão Lava a Outra ','Associações comunitárias',' Igrejas','Movimento Oeste ','Uma Mão Amiga',
           'Campos de futebol ']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [2.0, 2.0,2.0,1.0,1.0,1.0],
      theta=categories,
      fill='toself',
      name='Presença de espaços sociais organizados'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 2]
    )),
  showlegend=False
)

fig.show()