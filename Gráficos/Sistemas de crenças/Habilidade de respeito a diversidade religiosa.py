import matplotlib.pyplot as plt
import pandas as pd
from math import pi
# Set data
df = pd.DataFrame({
'name': ['John','David'],
'Respeito':  [3,3],
'Católicos': [2,2],
'Evangélicos':  [2,2],
'Candonblé':  [2,2],
'Congado to experience': [5, 1]})
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

ax.fill(angles, values, 'r', alpha=0.1)
# Add legend

ax.legend([' Habilidade de respeito a diversidade religiosa'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')

plt.title('Habilidade de respeito a diversidade religiosa\n ')
plt.show()