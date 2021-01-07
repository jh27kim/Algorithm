import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

g = sns.FacetGrid(col='who', row='survived', hue='sex', data=titanic)
print(g)
g.map(plt.hist, 'age')
plt.show()

import random
print(random.randint(1, 48))