
from cmath import pi

from matplotlib import pyplot as plt
classes = ['Projeto Uma Mão Lava a Outra  ','Associações comunitárias','Igrejas','Movimento Oeste ','Uma Mão Amiga','Campos de futebol']
data1 = [2.00, 2.00, 2.00, 1.00,1.00,1.00]
N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


data1 += data1[:1]
ax.fill(angles, data1, facecolor='orange', alpha=0.3)

ax.legend([' \nPresença de espaços sociais organizados\n'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Presença de espaços sociais organizados\n')


plt.show()






import plotly.graph_objects as go


classes = ['Faltam projetos coletivos  ','Horta coletiva','Projeto de psicultura']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[9,2,1],
    theta=classes,
    fill='toself',
    name='Participação coletiva comunitária na gestão de negócios',
    fillcolor="red", opacity=0.6, line=dict(color="red")

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