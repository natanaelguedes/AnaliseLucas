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

fig.show()