import plotly.graph_objects as go

categories20 = ['Coleta de lixo', 'Educação Ambiental', 'Reciclagem', 'Ferro velho','Lixeiras']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[3,3,2,2,2],
    theta=categories20,
    fill='toself',
    name='Gestão dos Resíduos Sólidos  ',
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