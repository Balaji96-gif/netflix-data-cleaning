import pandas as pd

df = pd.read_csv('netflix_titles.csv')
print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())

before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows.")

df['type'] = df['type'].str.strip().str.lower()
df['country'] = df['country'].str.title().fillna('Unknown')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
print(df['date_added'].head())

df[['duration_num', 'duration_unit']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
df['duration_num'] = pd.to_numeric(df['duration_num'], errors='coerce')


df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

df['release_year'] = df['release_year'].astype('int64')

df.to_csv('netflix_cleaned.csv', index=False)
print('Cleaned file saved.')
