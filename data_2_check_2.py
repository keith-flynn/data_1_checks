import pandas as pd

# Import goodreads data
df = pd.read_csv('assets/books.csv', on_bad_lines='skip')

# EDA
print(df.describe())
print(df.shape)
print(df.columns)
print(df.info())
print(df.head())

# num_pages column has leading spaces
df.rename(columns={"  num_pages": "num_pages"}, inplace=True)
print(df.columns)

# Even in the first five lines, some publisher jank is present
# i.e. Scholastic Inc and Scholastic are separate publishers
print(len(df['publisher'].unique()))
print(df['publisher'].unique())

# Converting 'Scholastic Inc.' to 'Scholastic'
print(df[df.publisher.str.contains('Scholastic')].head())
df.publisher.replace({'Scholastic Inc.':'Scholastic'}, regex=True,inplace=True)
print(df[df.publisher.str.contains('Scholastic')].head())
