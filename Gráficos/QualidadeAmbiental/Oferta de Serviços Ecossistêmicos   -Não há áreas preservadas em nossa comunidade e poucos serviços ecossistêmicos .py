from cmath import pi

from matplotlib import pyplot as plt
import plotly.graph_objects as go

categories = ['Muitas iniciativas','Lixo', 'Abandono','Racismo Ambiental']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[0],
      theta=categories,
      fill='toself',
      name='Oferta de Serviços Ecossistêmicos   - Não há áreas preservadas em nossa comunidade e poucos serviços ecossistêmicos',
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
