
import plotly.graph_objects as go


classes = ['Protagonismo feminino','Mulher forte','Mulher da favela','Mulher guerreira',
           'Mães solo','Mulher provedora','Violência doméstica','Creche']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,2,2,2,2,1,1,1],
    theta=classes,
    fill='toself',
    name='Valorização da mulher',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 7]
        )),
    showlegend=True
)

fig.show()