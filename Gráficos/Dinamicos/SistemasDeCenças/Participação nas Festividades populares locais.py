import plotly.graph_objects as go

categories = [' forró e bailes da terceira idade','Congado','Festa da colheita','festa dos estados','Festas Cosme e Damião',
              'Festas de São João ','festejos das igrejas evangélicas ','marcha pela paz ','Rap e Hip-hop','Samba e Pagode']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 1, 2, 1, 2,2,1,1,3,2],
      theta=categories,
      fill='toself',
      name='Participação nas Festividades populares locais'))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 3]
    )),
  showlegend=True
)

fig.show()