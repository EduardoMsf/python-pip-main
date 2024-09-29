import pandas as pd 
import numpy as np

df_books = pd.read_csv('/Users/jose.monsalvo/project/numpy-pandas/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')

def add_example():
    """
    This code demonstrates various operations on a pandas DataFrame.

    It reads a CSV file containing book data into a DataFrame, performs operations such as dropping columns and rows,
    adding new columns, and concatenating the DataFrame with itself.

    Returns:
        None
    """

    # Drop the 'Genre' column from the DataFrame
    df_books.drop(columns=['Genre'], axis=1, inplace=True)

    # Delete the 'Price' column from the DataFrame
    del df_books['Price']

    # Drop the first row from the DataFrame
    df_books.drop(0, axis=0)

    # Drop the first 10 rows from the DataFrame
    df_books.drop(range(0, 10), axis=0, inplace=True)

    # Add a new column named 'New Column' filled with NaN values
    df_books['New Column'] = np.nan

    # Add a new column named 'Rango' filled with a range of values
    data = np.arange(0, df_books.shape[0])
    df_books['Rango'] = data

    # Concatenate the DataFrame with itself
    new_data = pd.concat([df_books, df_books], axis=0)

    # Print the number of rows in the concatenated DataFrame
    print(new_data.shape[0])

# Call the function to execute the code
add_example()
import pandas as pd 
import numpy as np

df_books = pd.read_csv('/Users/jose.monsalvo/project/numpy-pandas/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')

# print(df_books.head(2))  # Print the data read from the CSV file

# #drop
# df_books.drop(columns=['Genre'], axis=1, inplace=True)
# print(df_books.head(2))  # Print the data read from the CSV file
# print(df_books.drop('Year', axis=1))  # Print the data read from the CSV file
# print(df_books.head(2))

# del df_books['Price']

# print(df_books.head(2))

# df_books.drop(0, axis=0)  # Print the data read from the CSV file
# print(df_books.head(2))


# df_books.drop(range(0,10), axis=0, inplace=True)  # Print the data read from the CSV file
# print(df_books.head(2))

#Add 
# df_books['New Column'] = np.nan
# print(df_books.head(2))  # Print the data read from the CSV file
# print(df_books.shape[0])

# data = np.arange(0, df_books.shape[0])
# df_books['Rango'] = data

# print(df_books.head(10)) 

new_data = pd.concat([df_books, df_books], axis=0)
print(new_data.shape[0])  # Print the data read from the CSV file

