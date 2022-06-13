from cmath import pi

from matplotlib import pyplot as plt
classes = ['Comércio local ','Influencers digitais','Excelentes prestadores de serviço ',
           'Comércio variado','Confiança','Vender fiado']
data1 = [3.00,2.00, 2.00, 2.00,1.00,1.00]
N = len(classes)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.clf()
ax = plt.subplot(polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], classes)


data1 += data1[:1]
ax.fill(angles, data1, facecolor='red', alpha=0.3)

ax.legend([' Valorização da economia local'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')
plt.title('Valorização da economia local\n')


plt.show()
