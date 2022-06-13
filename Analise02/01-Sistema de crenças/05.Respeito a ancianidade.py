
import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Respeito','Idoso','Recreação','Forró','MLI – Movimento de Luta dos Idosos','Projeto Raízes da Favela','Atendimento Psicológico','Bingo']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,3,2,2,2,2,1,1],
    theta=classes,
    fill='toself',
    name='Respeito a Ancianidade',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6]
        )),
    showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\01-Sistema de crenças\\image\\RespeitoAancianidade.jpg', format='png')

fig.show()