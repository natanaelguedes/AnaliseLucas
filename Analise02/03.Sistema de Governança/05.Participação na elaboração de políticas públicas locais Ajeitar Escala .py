


import plotly.graph_objects as go


classes = ['Participação comunitária','Orçamento participativo ','Obras',' Enchente']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2,1,1],
    theta=classes,
    fill='toself',
    name='Participação na elaboração de políticas públicas locais ',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6]
        )),
    showlegend=True
)

fig.show()