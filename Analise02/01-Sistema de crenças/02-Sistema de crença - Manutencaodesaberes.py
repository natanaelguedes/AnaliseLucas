

import plotly.graph_objects as go
from matplotlib import pyplot as plt
from pygments.formatters import img

categories20 = ['Cura','Cultivo chás medicinais','Dôlas','Benzedeira','Simpatia','Remédio']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[5,3,1,1,1,1],
    theta=categories20,
    fill='toself',
    name='Manutenção de saberes locais  ',
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

fig.show()

