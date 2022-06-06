from cmath import pi

from matplotlib import pyplot as plt
classes = ['Cura','Cultivos de chás medicinais','Dôlas','Benzedeira']
data1 = [1.00,1.00,1.00,1.00]

N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


data1 += data1[:1]
ax.fill(angles, data1, facecolor='blue', alpha=0.3)

ax.legend([' Participação nas Festividades populares locais'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Participação nas Festividades populares locais\n ')

plt.show()