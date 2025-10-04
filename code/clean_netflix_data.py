
import pandas as pd # imports pandas library (tables of data) = 'pd'


# df = data frame, table stored as variable df
df = pd.read_csv('data/netflix_titles.csv') # calls function to turn data set into table


print(df.shape) # returns tuple- (rows, columns)
print(df.head()) # shows first 5 rows of data

# info function- reveals column data types + column missing values
print(df.info()) # column names, data types, non-null value count

print(df.isnull().sum()) # OR use .isna
# checks every cell for missing data (NaN), adds column by column

print('Duplicate count before: ', df.duplicated().sum()) # .duplicated- if a row is identical to the previous= marks it true
df.drop_duplicates() # stores cleaned table without duplicates
print('Duplicates after: ', df.duplicated().sum()) # 'Duplicates after: 0'

df = df.dropna(subset= ['title', 'type']) # only removes rows with missing title OR type values
for col in ['director', 'cast', 'country', 'rating']: # starts loop with specific columns (col = placeholder variable)
    for col in df.columns: # checks whether column exists in data frame
        df[col] = df[col].fillna('Unknown') # replaces null values with 'Unknown', df[col]- indexes columns
# missing director/cast/country/rating = not critical to basic data analysis

print(df.isnull().sum()) # checks again how many null values are present

print(df['type'].value_counts()) # counts how many times each unique value appears in selected column

if 'rating' in df.columns: # IF condition
    print(df['rating'].value_counts().head(5)) # prints top 5 most common ratings
                                                    
print(df['release_year'].value_counts().head(5)) # prints top 5 release years

df.to_csv('data/netflix_titles_clean.csv', index = False) # saves data frame as CSV file, doesn't save row numbers
print('Saved cleaned dataset as "netflix_titles_clean.csv".') 
