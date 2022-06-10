import angles
import ax as ax
import plotly.graph_objects as go
from matplotlib import pyplot as plt


classes = ['Respeito','Católicos',' Evangélicos','Candonblé','Congado',
           'Espíritas ','Umbanda','marcha pela paz ','Sincretismo','Folia de reis']


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r= [3.0,2.0,2.0,2.0, 2.0,2.0,1.0,1.0,1.0,1.0],
      theta=classes,
      fill='toself',
      name='Habilidade de respeito a diversidade religiosa'
))
fig.show()