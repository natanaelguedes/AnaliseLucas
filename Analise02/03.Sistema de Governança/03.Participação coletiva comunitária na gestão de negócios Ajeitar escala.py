


import plotly.graph_objects as go


classes = ['Faltam projetos coletivos ','Horta coletiva','Projeto de psicultura ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[6,3,2],
    theta=classes,
    fill='toself',
    name='Participação coletiva comunitária na gestão de negócios',
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
