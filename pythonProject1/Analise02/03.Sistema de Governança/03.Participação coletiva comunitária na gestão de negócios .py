


import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Faltam projetos coletivos ','Horta coletiva','Projeto de piscicultura ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[9,2,1],
    theta=classes,
    fill='toself',
    name='Participação coletiva comunitária na gestão de negócios',
    fillcolor="yellow", opacity=0.6, line=dict(color="yellow")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 9]
        )),
    showlegend=True
)

fig.show()
