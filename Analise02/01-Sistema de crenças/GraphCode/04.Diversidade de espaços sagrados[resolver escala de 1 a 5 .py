import plotly.graph_objects as go




classes = ['Igreja católicas','Várias denominações evangélicas','Religiões afro-brasileiras','Centros espíritas']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[1,1,1,1],
    theta=classes,
    fill='toself',
    name='Habilidade de respeito a diversidade religiosa',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

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