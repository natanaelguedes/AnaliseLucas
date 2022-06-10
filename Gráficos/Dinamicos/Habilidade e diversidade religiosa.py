

import plotly.graph_objects as go

categories = ['Respeito','Católicos',' Evangélicos','Candonblé','Congado',
           'Espíritas ','Umbanda','marcha pela paz ','Sincretismo','Folia de reis']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [3.0,2.0,2.0,2.0, 2.0,2.0,1.0,1.0,1.0,1.0],
      theta=categories,
      fill='toself',
      name='Habilidade de respeito a diversidade religiosa'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=False
)

fig.show()