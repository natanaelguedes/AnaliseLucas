
import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Gerar renda','Economia circular ','Produção de máscaras','Falta de projetos']


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[2,1,1,1],
    theta=classes,
    fill='toself',
    name='Presença de projetos ou programas para geração de emprego e renda',
    fillcolor="yellow", opacity=0.6, line=dict(color="yellow")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 6]
        )),
    showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\Analise02\\02.Sistema Produtivo Local\\image\\Presença de projetos ou programas para geração de emprego e renda', format='png')

fig.show()