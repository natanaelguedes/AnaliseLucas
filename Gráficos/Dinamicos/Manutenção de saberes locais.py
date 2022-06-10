

import plotly.graph_objects as go
categories = ['Cura','Cultivos de chás medicinais','Dôlas','Benzedeira','Simpatia','Remédio']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [5.0, 3.0, 1.0,1.0,1.0],
      theta=categories,
      fill='toself',
      name='Manutenção de saberes locais'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

fig.show()