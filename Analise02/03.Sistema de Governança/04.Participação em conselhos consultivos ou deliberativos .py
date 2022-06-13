
from cmath import pi

from matplotlib import pyplot as plt
classes = ['Participação em conselhos ','Diminuição na participação','Conselhos perderam força']
data1 = [5.00, 2.00, 2.00]
N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


data1 += data1[:1]
ax.fill(angles, data1, facecolor='magenta', alpha=0.3)

ax.legend([' Participação na elaboração de políticas públicas locais '], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Participação em conselhos consultivos ou deliberativos\n')

plt.show()