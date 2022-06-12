import angles
import ax as ax
import plotly.graph_objects as go
from matplotlib import pyplot as plt

classes = ['igreja católicas ','Várias denominações evangélicas','Regiões afro-brasileira','Centro espíritas']
data1 = [1.00,1.00, 1.00,1.00]
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[5,3,1,1,1],
      theta=data1,
      fill='toself',
      name='Manutenção de saberes locais'
))


fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[1, 10]
    )),
  showlegend=False
)

data1 += data1[:1]

plt.legend([' Participação nas Festividades populares locais'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Participação nas Festividades populares locais\n ')
fig.show()