from cmath import pi

from matplotlib import pyplot as plt
classes = ['Respeito','Católicos',' Evangélicos','Candonblé','Congado',
           'Espíritas ','Umbanda','marcha pela paz ','Sincretismo','Folia de reis']
data1 = [3.0,2.0,2.0,2.0, 2.0,2.0,1.0,1.0,1.0,1.0]

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

ax.legend([' Habilidade de respeito a diversidade religiosa'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Habilidade de respeito a diversidade religiosa\n ')

plt.show()