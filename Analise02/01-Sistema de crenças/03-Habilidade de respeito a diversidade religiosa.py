


import plotly.graph_objects as go
from matplotlib import pyplot as plt
#
# categories20 = ['Respeito','Católicos','Evangélicos','Candonblé','Congado','Espiritas','Umbanda','Macha da paz',
#            'Sincretismo','Folia de reis']
categories20 = ['Respeito','Católicos','Evangélicos','Candonblé','Congado','Espiritas','Umbanda','Macha da paz',
           'Sincretismo','Folia de reis']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3.00,2.00,2.00,2.00,2.00,2.00,1.00,1.00,1.00,1.00],
    theta=categories20,
    fill='toself',
    name='Habilidade de respeito a diversidade religiosa',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 6]
        )),
    showlegend=True
)

plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\01-Sistema de crenças\\image\\Habilidade de respeito a diversidade religiosa', format='png')

fig.show()