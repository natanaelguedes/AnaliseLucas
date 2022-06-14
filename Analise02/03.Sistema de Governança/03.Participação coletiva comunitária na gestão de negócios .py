


import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Faltam projetos coletivos ','Horta coletiva','Projeto de psicultura ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[9,2,1],
    theta=classes,
    fill='toself',
    name='Participação coletiva comunitária na gestão de negócios',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 10]
        )),
    showlegend=True
)

fig.show()
