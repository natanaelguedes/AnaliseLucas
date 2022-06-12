

import plotly.graph_objects as go

categories = ['Participação comunitária',' Orçamento participativo ','Obras',' Enchente ']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [3.0, 2.0,1.0,1.0],
      theta=categories,
      fill='toself',
      name='Participação na elaboração de políticas públicas locais '))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=True
)

fig.show()