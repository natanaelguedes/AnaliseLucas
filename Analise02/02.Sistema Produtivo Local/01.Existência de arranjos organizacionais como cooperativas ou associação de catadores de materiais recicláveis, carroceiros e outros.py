
import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Negócios de reciclagem','Feiras de alimentos ','Carroceiros','Cooperativismo']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[2,2,1,1],
    theta=classes,
    fill='toself',
    name="Existência de arranjos organizacionais como cooperativas ou associação de catadores de materiais recicláveis, carroceiros e outros",
    fillcolor="yellow", opacity=0.6, line=dict(color="yellow")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,3]
        )),
    showlegend=True
)

fig.show()