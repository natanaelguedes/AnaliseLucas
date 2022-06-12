

import plotly.graph_objects as go


classes = ['Protagonismo feminino','Mulher forte','Mulher da favela','Mulher guerreira','Mães solo','Mulher provedora','Violência doméstica','Creche']


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r = [4.00,2.00,2.00,2.00, 2.00,1.00,1.00,1.00],
      theta=classes,
      fill='toself',
      name='Respeito a Ancianidade'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 4]
    )),
  showlegend=True
)

fig.show()