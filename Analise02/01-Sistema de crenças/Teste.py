import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[1,1,2,1,2,2,1,1,3,2],
    theta=[' forró e bailes da terceira idade','Congado','Festa da colheita',
           'festa dos estados', 'Festas Cosme e Damião','Festas de São João ',
           'festejos das igrejas evangélicas','marcha pela paz ','Rap e Hip-hop',
           'Samba e Pagode']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()