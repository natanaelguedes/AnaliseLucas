from cmath import pi

from matplotlib import pyplot as plt
classes =[' forró e bailes da terceira idade','Congado','Festa da colheita','festa dos estados',
              'Festas Cosme e Damião', 'Festas de São João ',' festejos das igrejas evangélicas ','marcha pela paz ','Rap e Hip-hop',
              'Samba e Pagode']
r = [1, 1, 2, 1, 2, 2, 1, 1, 3, 2],

N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


classes += classes[:1]
ax.fill(angles, classes, facecolor='blue', alpha=0.3)

ax.legend([' Manutenção de saberes locais'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Manutenção de saberes locais\n ')

plt.show()