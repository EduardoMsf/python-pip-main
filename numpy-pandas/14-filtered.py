import pandas as pd 

df_books = pd.read_csv('/Users/jose.monsalvo/project/numpy-pandas/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)
print(df_books.head(2))  # Print the data read from the CSV filed
mayor_a_2016 = df_books['Year'] > 2016  # Create a filter
print(df_books[mayor_a_2016])  # Print the result of the filter

genre_fiction = df_books['Genre'] == 'Fiction'  # Create a filter
print(df_books[genre_fiction & mayor_a_2016])  # Print the result of the filter
print(df_books[~mayor_a_2016])  # Print the result of the filter