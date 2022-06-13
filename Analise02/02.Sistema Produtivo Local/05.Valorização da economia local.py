

import plotly.graph_objects as go



classes = ['Comércio local ','Influencers digitais','Excelentes prestadores de serviço ',
           'Comércio variado','Confiança','Vender fiado']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,2, 2, 2,1,1],
    theta=classes,
    fill='toself',
    name='Valorizaçao de economia local',
    fillcolor="yellow", opacity=0.6, line=dict(color="yellow")

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