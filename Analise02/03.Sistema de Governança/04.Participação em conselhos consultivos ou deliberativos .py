


import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Participação em conselhos','Diminuição na participação','Conselhos perderam força']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[5,2,2],
    theta=classes,
    fill='toself',
    name='Participação em conselhos consultivos ou deliberativos',
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