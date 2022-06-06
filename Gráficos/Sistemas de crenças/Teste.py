import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dosyayi oku

# Stat sutunlarini al
cols = [ "hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]

# 3. sirada Charmander var

# 360 dereceyi uygun sekilde bol
angles=np.linspace(0, 1*np.pi, len(cols), endpoint=False)



# Veri kumesinin sonuna ilk noktayi ekleyerek birlestirmeye zorluyoruz

# Radar chart
fig = plt.figure()
ax = fig.add_subplot(111, polar=True) # polar argumani onemli

ax.set_thetagrids(angles * 180/np.pi, cols)

plt.show()