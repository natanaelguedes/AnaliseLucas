

import plotly.graph_objects as go

categories = ['Participação em conselhos',' Diminuição na participação ','Conselhos perderam força ']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [5.0, 2.0,2.0],
      theta=categories,
      fill='toself',
      name='Participação em conselhos consultivos ou deliberativos'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True
)

fig.show()