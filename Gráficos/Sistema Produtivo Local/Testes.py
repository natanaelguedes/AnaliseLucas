import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
from math import pi
import io
df = pd.read_csv(io.StringIO("""category	A	B
Antisocial attitudes	6	7
Antisocial peers	3	6
Antisocial personality	6	2
History of antisocial behaviour	1	4
Family	8	1
Education/employment	2	7
Substance abuse	2	3"""), sep='\t')
df


def do_plot(df, col, color, ax):
    # based on
    categories = list(df['category'])
    values = list(df[col])
    values += values[:1] # repeat the first value to close the circular graph
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]


    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticks(np.arange(0, len(categories)))
    ax.set_ylim(0, 5)
    ax.set_rlabel_position(30)

    ax.plot(angles, values, linewidth=1, color=color, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    do_plot(df=df, col='B', color='red', ax=ax)
    do_plot(df=df, col='A', color='blue', ax=ax)
    fig.show()