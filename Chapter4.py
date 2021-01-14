import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import preprocessing
import sys

titanic = sns.load_dataset('titanic')
df = titanic[['age', 'sex', 'class', 'fare', 'survived']]

pdf3 = pd.pivot_table(df,
                     index=['class', 'sex'],
                     columns='survived',
                     values=['age', 'fare'],
                     aggfunc=['mean', 'max'])

print(pdf3.head(6))

print(pdf3.xs(('max', 'fare', 0),
              level=[0, 1, 2], axis=1))

print(pdf3.xs(('max', 'fare', 1), level=[0,1,2], axis=1))

import random
print(random.randint(1, 48))