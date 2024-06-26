# -*- coding: utf-8 -*-
"""netflix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Z5rr8-z3I4nussG1mDhsCXBl5dpx9s_
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sn

path = "/content/imdb_data.csv"

data = pd.read_csv(path)

data.head()

data [['Title', 'Year']] = data['Name'].str.extract(r'(.+)\s\((\d{4})\)')

data = data.drop("Name" , axis = 1)

data.head()

data.info()

data['Year'] = pd.to_numeric(data['Year'])

plt.hist(data['Rating'], bins=20, alpha=0.7)
plt.title('Distribution of IMDb Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()

old_movie = data[(data["Year"] > 1980) & (data["Year"] < 2000)]
data = data[data["Year"] > 2000]

plt.figure(figsize=(20,10))
sn.barplot(data , x = "Year" , y = "Rating" , errorbar=None)

plt.figure(figsize=(10, 10))
plt.pie(old_movie["Year"].value_counts(), labels=old_movie["Year"].value_counts().index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Ratings for Old Movies')
plt.axis('equal') 