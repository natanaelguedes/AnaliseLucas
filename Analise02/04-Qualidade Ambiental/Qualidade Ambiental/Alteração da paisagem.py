import plotly.graph_objects as go

categories20 = ['Piorou', 'Progresso', 'Meio Ambiente', 'Necessário']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,2,2, 2],
    theta=categories20,
    fill='toself',
    name='Alteração da paisagem',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,5]
        )),
    showlegend=True
)

fig.show()