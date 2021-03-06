import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Igreja católicas','Várias denominações evangélicas','Religiões afro-brasileiras','Centros espíritas']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[1,1,1,1],
    theta=classes,
    fill='toself',
    name='Diversidade de espaços sagrados ',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 3]
        )),
    showlegend=True
)


fig.show()