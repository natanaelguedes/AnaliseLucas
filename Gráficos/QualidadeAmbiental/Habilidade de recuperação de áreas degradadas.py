from cmath import pi

from matplotlib import pyplot as plt
import plotly.graph_objects as go

categories = ['Muitas iniciativas','Lixo', 'Abandono','Racismo Ambiental']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[ 4,2, 2,1],
      theta=categories,
      fill='toself',
      name='Habilidade de recuperação de áreas degradadas',
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
