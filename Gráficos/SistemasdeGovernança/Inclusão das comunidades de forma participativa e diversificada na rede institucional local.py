

import plotly.graph_objects as go

categories = ['Comunidade atuante ','Voluntarios',' Associação 1° de Maio ']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [6.0, 3.0,2.0],
      theta=categories,
      fill='toself',
      name='Inclusão das comunidades de forma participativa e diversificada na rede institucional local'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 6]
    )),
  showlegend=False
)

fig.show()