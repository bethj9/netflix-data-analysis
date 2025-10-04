

import pandas as pd # library to use tables of data
import matplotlib.pyplot as plt # library to make charts/graphs


df = pd.read_csv('data/netflix_titles_clean.csv') # loads clean data set through file path


# first visualisation = movie vs tv shows count

type_counts = df['type'].value_counts() # counts how many times each unique value appears in the column

plt.figure(figsize=(6, 4)) # creates a new figure (blank page for chart), 6 x 4 inches
type_counts.plot(kind='bar') # argument calling a vertical bar chart
# plot method attached to variable 'type_counts'
plt.title('Count of movies vs TV shows') # bar chart title
plt.xlabel('Type') # x axis label
plt.ylabel('Number of Titles') # y axis label

plt.show() # displays the figure


# second visualisation = top 5 release years

year_counts = df['release_year'].value_counts().head(5) # creates variable of top 5 release year dates

plt.figure(figsize=(6,4)) # creates figure (4 x 6 inches)
year_counts.plot(kind='bar') # plots bar chart
plt.title('Top 5 Release Years on Netflix') # sets title
plt.xlabel('Release year') # x axis label
plt.ylabel('Number of Titles') # y axis label

plt.show() 


# third visualisation = movies vs tv shows

type_counts = df['type'].value_counts().head(5)

plt.figure(figsize=(6,6)) 
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90) 
# labels slices with movie / TV show, percentage on each slice to 1.d.p., rotates pie to start at top
plt.title('Percentages of Movies vs TV Shows on Netflix')

plt.show()