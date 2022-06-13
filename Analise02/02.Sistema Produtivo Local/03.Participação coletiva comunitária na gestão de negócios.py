
import plotly.graph_objects as go


classes = ['Gerar renda','Economia circular ','Produção de máscaras','Falta de projetos']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[2,1,1,1],
    theta=classes,
    fill='toself',
    name='Presença de projetos ou programas para geração de emprego e renda',
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