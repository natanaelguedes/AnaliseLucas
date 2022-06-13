
from cmath import pi

from matplotlib import pyplot as plt
classes = ['Ribeirão Arrudas ','Poluição','Mina','Inundação']



fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,4,3,2],
    theta=classes,
    fill='toself',
    name='Conservação de mananciais',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 6]
        )),
    showlegend=True
)

fig.show()