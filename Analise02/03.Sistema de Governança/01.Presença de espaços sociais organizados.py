




import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Projeto Uma Mão Lava a Outra ','Associações comunitárias',
           'Igrejas','Movimento Oeste  ','Uma Mão Amiga','Campos de futebol']


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[2,2, 2, 1,1,1],
    theta=classes,
    fill='toself',
    name='Presença de espaços sociais organizados',
    fillcolor="red", opacity=0.6, line=dict(color="red")

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