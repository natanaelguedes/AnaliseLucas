

import plotly.graph_objects as go
from matplotlib import pyplot as plt
from pygments.formatters import img

categories20 = ['Respeito','Católicos','Evangélicos','Candonblé','Congado','Espiritas','Umbanda','Macha da paz',
           'Sincretismo','Folia de reis']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2,2,2,2,2,1,1,1,2],
    theta=categories20,
    fill='toself',
    name='Manutenção de saberes locais  ',
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

fig.show()

plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\02-Sistema de crenças\\image\\Manutencaodesaberes.jpg', format='png')
