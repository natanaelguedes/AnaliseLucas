import plotly.graph_objects as go

categories13 = ['Projeto Uma Mão Lava a Outra', 'Associações comunitárias', 'Igrejas', 'Movimento Oeste ', 'Uma Mão Amiga', 'Campos de futebol']
categories14 = ['Comunidade Atuante', 'Voluntários', 'Associação 1° de Maio ']
categories15 = ['Faltam projetos coletivos', 'Horta coletiva', 'Projeto de psicultura']
categories16 = ['Participação em conselhos', ' Diminuição na participação ', 'Conselhos perderam força']
categories17 = ['Comunidade participa', ' Abaixo assinado ', 'Ocupação', 'Solicitação comunitária']
categories18 = ['Dialoga bem','Representatividade','Comunidade','Resistências']
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[2,2,2,1,1, 1],
    theta=categories13,
    fill='toself',
    name='Presença de espaços sociais organizados',
))


fig.add_trace(go.Scatterpolar(
      r=[6,3,2],
      theta=categories14,
      fill='toself',
      name='Inclusão das comunidades de forma participativa e diversificada na rede institucional local',
))


fig.add_trace(go.Scatterpolar(
      r=[9,2,1],
      theta=categories15,
      fill='toself',
      name='Participação coletiva comunitária na gestão de negócios',
))



fig.add_trace(go.Scatterpolar(
      r=[5,3,2,2],
      theta=categories16,
      fill='toself',
      name='Participação nas tomadas de decisões coletivas',
))

fig.add_trace(go.Scatterpolar(
    r=[3, 2,1, 1],
    theta=categories17,
    fill='toself',
    name=' Participação na elaboração de políticas públicas locais',
))


fig.add_trace(go.Scatterpolar(
    r=[3, 2,2, 1],
    theta=categories18,
    fill='toself',
    name=' Habilidade das comunidades em interagir de modo intersetorial',
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 5]
        )),
    showlegend=False
)


fig.show()