from cmath import pi

from matplotlib import pyplot as plt



import plotly.graph_objects as go
from pygments.formatters import img

categories20 = [' forró e bailes da terceira idade','Congado','Festa da colheita','festa dos estados',
                'Congado','Festas Cosme e Damião','Festas de São João ','festejos das igrejas evangélicas ',
           'marcha pela paz ','Rap e Hip-hop',' Samba e Pagode']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[1,1,2,1,2,2,1,1,3,2],
    theta=categories20,
    fill='toself',
    name='Participação nas Festividades populares locais',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 4]
        )),
    showlegend=True
)
plt.savefig('teste.png', format='png')

fig.show()

