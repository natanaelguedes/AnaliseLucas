
import plotly.graph_objects as go


classes = ['Respeito','Idoso','Recreação','Forró','MLI – Movimento de Luta dos Idosos','Projeto Raízes da Favela','Atendimento Psicológico','Bingo']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[4,3,2,2,2,2,1,1],
    theta=classes,
    fill='toself',
    name='Respeito a Ancianidade',
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