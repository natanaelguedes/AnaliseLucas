




import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Projeto Uma Mão Lava a Outra ','Associações comunitárias',
           'Igrejas','Movimento Oeste  ','Uma Mão Amiga','Campos de futebol']


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[2,2, 2, 1,1,1],
    theta=classes,
    fill='toself',
    name='Valorizaçao de economia local',
    fillcolor="yellow", opacity=0.6, line=dict(color="yellow")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 6]
        )),
    showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\Analise02\\03.Sistema de Governança\\image\\presenca espaços organizados', format='png')

fig.show()