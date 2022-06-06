import matplotlib.pyplot as plt
import pandas as pd
from math import pi
# Set data
df = pd.DataFrame({
'name': ['John','David'],
'Igrejas católicas':  [1, 1],
'Várias denominações evangélicas': [1, 1],
'Religiões afro-brasileiras':  [1, 1],
'Centros espíritas': [1,1]})

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
plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="black", size=7)
plt.ylim(0,5)
# ------- PART 2: Add plots
# Name1
values=df.loc[0].drop('name').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="John")
ax.fill(angles, values, 'b', alpha=0.1)ax.fill(angles, values, facecolor='blue', alpha=0.3)

# Name2

# Add legend
ax.legend([' Diversidade de espaços sagrados'], loc=(0.9, .95),  labelspacing=0.1, fontsize='small')
plt.title(' Diversidade de espaços sagrados\n ')
plt.show()