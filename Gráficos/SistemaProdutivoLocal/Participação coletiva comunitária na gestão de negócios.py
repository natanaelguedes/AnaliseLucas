import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[1,1,2,1,2,2,1,1,3,2],
    theta=['Forró e bailes da terceira idade','Festa da Colheita','Festa dos estados',
           'Festa Cosme e Damião', 'Festas de São João','Festejos das igrejas evangélicas','Marcha pela paz'
           'Rap e Hip-hop','Samba e Pagode']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()