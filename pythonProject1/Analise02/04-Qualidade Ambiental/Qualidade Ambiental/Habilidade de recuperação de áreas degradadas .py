import plotly.graph_objects as go

categories20 = ['Educação ambiental','Muitas iniciativas', 'Lixo', 'Abandono', 'Racismo Ambiental']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[1,4,2,2, 1],
    theta=categories20,
    fill='toself',
    name='Habilidade de recuperação de áreas degradadas',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

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