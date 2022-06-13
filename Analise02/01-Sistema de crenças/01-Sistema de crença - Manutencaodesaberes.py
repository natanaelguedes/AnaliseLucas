

import plotly.graph_objects as go

categories20 = ['Respeito','Católicos','Evangélicos','Candonblé','Congado','Espiritas','Umbanda','Macha da paz',
           'Sincretismo','Folia de reis']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2,2,2,2,2,1,1,1,2],
    theta=categories20,
    fill='toself',
    name='Manutenção de saberes locais  ',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

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