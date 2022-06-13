
from cmath import pi

from matplotlib import pyplot as plt
classes = ['Comunidade Atuante ','Voluntários','Associação 1° de Maio ']
data1 = [6.00, 3.00, 2.00]
N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


data1 += data1[:1]
ax.fill(angles, data1, facecolor='orange', alpha=0.3)

ax.legend([' Inclusão das comunidades de forma participativa \ne diversificada na rede institucional local'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Inclusão das comunidades de forma participativa e diversificada na rede institucional local\n' )

plt.show()