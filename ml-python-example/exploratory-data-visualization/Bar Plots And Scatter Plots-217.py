## 2. Introduction to the data ##

import pandas as pd
reviews=pd.read_csv('fandango_scores.csv')
norm_reviews['FILM']=reviews['FILM']
norm_reviews['RT_user_norm']=reviews['RT_user_norm']
norm_reviews['Metacritic_user_nom']=reviews['Metacritic_user_nom']

norm_reviews['IMDB_norm']=reviews['IMDB_norm']

norm_reviews['Fandango_Ratingvalue']=reviews['Fandango_Ratingvalue']

norm_reviews['Fandango_Stars']=reviews['Fandango_Stars']
norm_reviews[1:]

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews.ix[0, num_cols].values
print(bar_heights)
bar_positions = arange(5) + 0.75
fig,ax=plt.subplots()
ax.bar(bar_positions,bar_heights,0.5)
plt.show()

## 5. Aligning Axis Ticks And Labels ##

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig,ax=plt.subplots()
ax.bar(bar_positions,bar_heights,0.5)


ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols,rotation=90)


plt.xlabel('Rating Source')
plt.ylabel('Average Rating')
plt.title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

## 6. Horizontal Bar Plot ##

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5)

ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title('Average User Rating for Avengers: Age of Ultron (2015)')
plt.show()

## 7. Scatter plot ##

fig,ax=plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
plt.xlabel('Fandango')
plt.ylabel('Rotten Tomatoes')
plt.show()

## 8. Switching axes ##

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango_Ratingvalue')
ax1.set_ylabel('Rottan Tommatoes')
ax2.scatter(norm_reviews['RT_user_norm'],norm_reviews['Fandango_Ratingvalue'])
ax2.set_ylabel('Fandango_Ratingvalue')
ax2.set_xlabel('Rottan Tommatoes')
plt.show()

## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Totten Tomatoes')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)


ax3.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['IMDB_norm'])
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)

plt.show()