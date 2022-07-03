


import plotly.graph_objects as go

categories = ['Faltam áreas preservadas', 'Poucos serviços ecossistêmicos']
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[4, 3],
      theta=categories,
      fill='toself',
      name='Oferta de Serviços Ecossistêmicos',
      fillcolor="orange", opacity=0.6, line=dict(color="orange")

))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True
)

fig.show()