from cmath import pi

from matplotlib import pyplot as plt
import plotly.graph_objects as go

categories = ['Ribeirão Arrudas','Poluição', 'Mina','Inundação']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[4,4, 3, 2],
      theta=categories,
      fill='toself',
      name='Conservação de mananciais',
      fillcolor='tomato'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 4]
    )),
  showlegend=True
)

fig.show()
