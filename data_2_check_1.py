import requests
import pandas as pd
import json

# Pull in data from an API
# Parse - serialize a get request
data_url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
response = requests.get(data_url)
# 200 is response code for success
print(response)

# Raw response
response_dict = response.json()
print(response_dict)

# Access content as a dictionary
data_section = response_dict.get('data')
print(data_section)

# Easier to visualize
pretty = json.dumps(response_dict, indent=4)
print(pretty)

# Bring it all into a pandas dataframe
df = pd.DataFrame(response_dict.get('data'))
# Find and print TWO descriptive statistics about your data.
print(list(df))
print(df.describe())
print(df)

# Drop superfluous columns
df_dropped = df.drop(['ID Nation', 'ID Year', 'Slug Nation'], axis=1)
print(df_dropped)

# Find and print TWO descriptive statistics about your data.
# Not sure if my prior one fulfills Knowledge Check requirements, 
# so I'm adding a couple more.
shape = df.shape
print('Number of columns: \n', shape[1])
print('Number of rows: \n', shape[0])
pop_mean = df['Population'].mean()
print('Population mean: \n', pop_mean)

# Write a query in Pandas to select a particular set of your data.
over_amount = df_dropped.where(df_dropped['Population'] > 315000000)
print(over_amount.dropna())

# Select and print the SECOND AND THIRD columns of your data frame.
print(df.iloc[:, 1:3])

# Select and print the FIRST 4 rows of your data frame.
print(df.head(4))