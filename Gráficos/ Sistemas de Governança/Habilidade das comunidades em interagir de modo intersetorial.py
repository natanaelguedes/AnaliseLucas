

import plotly.graph_objects as go

categories = ['Dialoga bem','Representatividade',' Comunidade','Resistências']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [3.0,2.0, 2.0,1.0],
      theta=categories,
      fill='toself',
      name='Habilidade das comunidades em interagir de modo intersetorial'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=True
)

fig.show()