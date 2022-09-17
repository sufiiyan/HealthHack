import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('Tuberculosis_final.csv')

x = df['cases']
y = df['Districts']

plt.title('Plot for Tuberculosis Death Numbers')
plt.xlabel('Cases')
plt.ylabel('Districts')
plt.plot(x, y)
