import plotly.graph_objects as go
from matplotlib import pyplot as plt

categories20=[' Forró e bailes da terceira idade ','Congado','Festa da colheita',
           'Festa dos estados', 'Festas Cosme e Damião',' Festas de São João ',
           'Festejos das igrejas evangélicas ','Marcha pela paz','Rap e Hip-hop',
           'Samba e Pagode']
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[1, 1, 2, 1,2,2,1,1, 3,2],
    theta=categories20,
    fill='toself',
    name='Participação nas Festividades populares locais  ',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

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