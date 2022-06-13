


import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Comunidade participa','Abaixo assinados ','Ocupação',' Solicitação comunitária ']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[5,3,2,2],
    theta=classes,
    fill='toself',
    name='Participação nas tomadas de decisões coletivas',
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
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\Analise02\\03.Sistema de Governança\\image\\Participação nas tomadas de decisões coletivas', format='png')

fig.show()