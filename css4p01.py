# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:16:56 2024

@author: Axhoba Ntoni
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("movie_dataset.csv")

print(df.isnull().sum())

print(df)
df.columns = df.columns.str.replace(' ','_')
print(df)

#df.dropna(inplace=True)
# For "Revenue_(Millions)" 
df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean(), inplace=True)

# For "Metascore" 
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)
print(df.isnull().sum())


#############################################################

#df.reset_index(drop=True, inplace=True)

print("Question 1 \n")

highest_rated_movie = df.loc[df['Rating'].idxmax()]

# Print the details of the highest-rated movie
print("Highest Rated Movie:")
print("Title:", highest_rated_movie['Title'])
print("Rating:", highest_rated_movie['Rating'])


#Q2
print("Question 2 \n")
# Assuming 'df' is the cleaned dataset
average_revenue = df['Revenue_(Millions)'].mean()

# Print the average revenue
print("Average Revenue of All Movies:", average_revenue)

#3
print("Question 3 \n")
# Assuming 'df' is the cleaned dataset
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = filtered_movies['Revenue_(Millions)'].mean()

# Print the average revenue for movies from 2015 to 2017
print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_2017)


#Q4 
print("Question 4 \n")



movies_2016 = len(df.loc[df['Year'] == 2016])


print("Number of Movies Released in 2016:", movies_2016)

#Q5
print("Question 5 \n")

movies_by_nolan = df['Director'].value_counts().get('Christopher Nolan', 0)
print("Number of Movies Directed by Christopher Nolan:", movies_by_nolan)


#Q6
print("Question 6 \n")
highly_rated_movies = len(df.loc[df['Rating'] >= 8.0])
print("Number of Movies with a Rating of at least 8.0:", highly_rated_movies)


#7
print("Question 7 \n")
nolan_movies = df.loc[df['Director'] == 'Christopher Nolan']
median_rating_nolan = nolan_movies['Rating'].median()
print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan)

#8
print("Question 8 \n")
average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print("Year with the Highest Average Rating:", year_highest_average_rating)
print("Highest Average Rating:", highest_average_rating)


#9
print("Question 9 \n")
movies_2006 = len(df[df['Year'] == 2006])
movies_2016 = len(df[df['Year'] == 2016])

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"Percentage Increase in Number of Movies (2006 to 2016): {percentage_increase:.2f}%")
print("\n")

#10
print("Question 10 \n")
all_actors = df['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]
print("Most Common Actor in All Movies:", most_common_actor)



#Q11
print("Question 10 \n")
unique_genres = df['Genre'].str.split(', ').explode().unique()
num_unique_genres = len(unique_genres)

print("Number of Unique Genres:", num_unique_genres)



#Q12
print("Question 11 \n")
numeric_columns = df.select_dtypes(include=['number'])

correlation_matrix = numeric_columns.corr()
print("Correlation Matrix:")
print(correlation_matrix)




