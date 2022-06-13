from cmath import pi

from matplotlib import pyplot as plt



import plotly.graph_objects as go
from pygments.formatters import img

categories20 = ['Respeito','Católicos','Evangélicos','Candonblé','Congado','Espiritas','Umbanda','Macha da paz',
           'Sincretismo','Folia de reis']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2,2,2,2,2,1,1,1,1],
    theta=categories20,
    fill='toself',
    name='Habilidade de respeito a diversidade religiosa',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 4]
        )),
    showlegend=True
)

fig.show()
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\01-Sistema de crenças\\image\\Participacaonasfestividades.jpg', format='png')


