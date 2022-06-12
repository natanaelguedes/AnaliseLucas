import plotly.graph_objects as go

categories = ['Coleta  de Lixo','Educação Ambiental', 'Reciclagem','Ferro velho','Lixeiras']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[ 3, 3, 2,2,2],
      theta=categories,
      fill='toself',
      name='Gestão dos Resíduos Sólidos ',
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
