


import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Dialoga bem','Representatividade ','Comunidade',' Resistências ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2,2,1],
    theta=classes,
    fill='toself',
    name='Habilidade das comunidades em interagir de modo intersetorial',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 6]
        )),
    showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\Analise02\\03.Sistema de Governança\\image\\Habilidade das comunidades em interagir de modo intersetorial', format='png')

fig.show()