


import plotly.graph_objects as go


classes = ['Comunidade Atuante ','Voluntários','Associação 1° de Maio ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[6,3,2],
    theta=classes,
    fill='toself',
    name='Inclusão das comunidades de forma participativa e diversificada na rede institucional local',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 8]
        )),
    showlegend=True
)

fig.show()
