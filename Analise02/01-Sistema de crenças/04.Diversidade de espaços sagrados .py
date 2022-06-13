import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['Igreja católicas','Várias denominações evangélicas','Religiões afro-brasileiras','Centros espíritas']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[1,1,1,1],
    theta=classes,
    fill='toself',
    name='Habilidade de respeito a diversidade religiosa',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 3]
        )),
    showlegend=True
)

plt.savefig('C:\\Users\\natan\\PycharmProjects\\Antigo\\Analise02\\04-Sistema de crenças\\image\\DiversidadesDeEspacosSagrados', format='png')

fig.show()