from tkinter import font

import plotly.graph_objects as go
from matplotlib import pyplot as plt
from numpy import size

categories = ['Igrejas católicas','Várias denominações evangélicas','Religiões afro-brasileiras',
              'Centros espíritas']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 1, 1, 1, 1],
      theta=categories,
      fill='toself',
      name='Diversidade de espaços sagrados'
))


fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 1]
    )),
  showlegend=True
)
plt.savefig('C:\\Users\\natan\\PycharmProjects\\AnaliseLucas\\Gráficos\\Dinamicos\\Imagens\\Sistemasdecrencas\\Diversidedade e espaços sagrados.png', format='png')

fig.show()