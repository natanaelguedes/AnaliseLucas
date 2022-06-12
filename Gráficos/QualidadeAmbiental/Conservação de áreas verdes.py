import plotly.graph_objects as go

categories = ['Arborização','Área verde', 'Cemiterio da Colina']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[ 3, 3, 2],
      theta=categories,
      fill='toself',
      name='Conservação de áreas verdes',
      fillcolor='tomato'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=True
)

fig.show()
