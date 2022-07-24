
import matplotlib.pyplot as plt
plt.title('Oferta de Serviços Ecossistêmicos')
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels =  ['Faltam áreas preservadas', 'Poucos serviços ecossistêmicos']
sizes = [4, 3]

plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


