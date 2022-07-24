import plotly.graph_objects as go

categories20 = ['Faltam áreas preservadas', 'Poucos serviços ecossistêmicos','Falta arborização']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,3,2],
    theta=categories20,
    fill='toself',
    name='Oferta de Serviços Ecossistêmicos',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5]
        )),
    showlegend=True
)

fig.show()