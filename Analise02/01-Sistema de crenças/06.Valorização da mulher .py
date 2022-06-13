
import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Protagonismo feminino','Mulher forte','Mulher da favela','Mulher guerreira',
           'Mães solo','Mulher provedora','Violência doméstica','Creche']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,2,2,2,2,1,1],
    theta=classes,
    fill='toself',
    name='Valorização da mulher',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 7]
        )),
    showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\01-Sistema de crenças\\image\\ValorizaçãoDaMulher.jpg', format='png')

fig.show()