import pandas as pd
path = './population_by_age_sex_year.csv'
data = pd.read_csv(path)

df = pd.DataFrame(data=data)

#remove invalid data
df = df[[(len(x) < 3) for x in df['age']]]

#split data
cols = ['men', 'women','age']
df[cols] = df[cols].apply(pd.to_numeric, downcast='integer', errors='coerce', axis=1)

df['population'] = df['women'] + df['men']
df = df.drop(['women', 'men'], axis=1)

df.insert(loc=0, column='group', value="")

df.loc[df['age'] > 65, 'group'] = "65-80"
df.loc[df['age'] < 19, 'group'] = "0-20"
df.loc[df['group'] == "", 'group'] = "20-65"

df.to_csv('preprocessed_population.csv', sep=',')
