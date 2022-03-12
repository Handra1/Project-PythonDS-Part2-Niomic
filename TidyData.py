import pandas as pd
df = pd.read_csv('C:/Users/Handra/Documents/Data Science/tidy_data.csv')
print(pd.melt(frame=df, id_vars='Name', value_vars=['treatment a','treatment b']))
print(pd.melt(frame=df, id_vars='Name', value_vars=['treatment a','treatment b'],
var_name = 'Treatment', value_name='Results'))
