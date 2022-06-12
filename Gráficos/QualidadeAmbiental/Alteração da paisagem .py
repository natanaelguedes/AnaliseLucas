import plotly.graph_objects as go

categories = ['Piorou','Progresso', 'Meio Ambiente','Necessário']

fig = go.Figure()


fig.add_trace(go.Scatterpolar(
      r=[ 4,2, 2,2],
      theta=categories,
      fill='toself',
      name='Alteração da paisagem',
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
