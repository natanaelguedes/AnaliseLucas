import matplotlib.pyplot as plt
import pandas as pd
from math import pi
# Set data
df = pd.DataFrame({
'name': ['John','David'],
' forró e bailes da terceira idade':[1,1],
'Congado': [1,1],
'Festa da colheita':  [1,1],
'Festa dos estados':  [1,1],
'Festas Cosme e Damião': [2, 2],
'Festa de São João':[2,2],
'Festejos das igrejas evangélicos':[1,1],
'Marcha pela paz':[1,1],
'Rap e Hip-hop':[3,3],
'Samba e Pagode':[2,2]})
categories=list(df)[1:]
N = len(categories)
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
plt.ylim(0,5)
# ------- PART 2: Add plots
# Name1
values=df.loc[0].drop('name').values.flatten().tolist()
values += values[:1]

# ax.fill(angles, values, 'b', alpha=0.1)
# Name2
values=df.loc[1].drop('name').values.flatten().tolist()
values += values[:1]


# Add legend
ax.fill(angles, values, facecolor='blue', alpha=0.3)

ax.legend([' Participação nas Festividades populares locais'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Participação nas Festividades populares locais\n ')
plt.show()