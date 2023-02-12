import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('assets/cereal.csv', usecols=['name', 'calories'])

plt.style.use('dark_background')
# Sort by calories descending
df_sorted = df.sort_values(by='calories', ascending=False)
plt.figure(figsize=(15, 7))
# Slicing out the first ten rows because of the sheer number of all cereals
plt.bar(df_sorted.name.iloc[0:9], df_sorted.calories.iloc[0:9])
plt.xticks(rotation=45, fontsize=9)
plt.title('Top 10 Breakfast Cereals Ranked by Calories per Serving')
plt.ylabel('Calories per Serving')
plt.tight_layout()
plt.show()