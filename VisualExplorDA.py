import pandas as pd
df = pd.read_csv('data2.csv')
print(df.info())
print(df.describe())
df['population'] = df.population.str.replace(',','').astype(float)
print(df.info())
print(df.describe())

print(df.population.plot(kind='hist'))

import matplotlib.pyplot as plt
plt.show()

print(df[df.population > 1000000000])

print(df.boxplot(column='population', by='Continent'))
plt.show()
