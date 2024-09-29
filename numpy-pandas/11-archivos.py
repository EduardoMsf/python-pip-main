import pandas as pd 

def read_csv_file(file_path):
    """
    Read a CSV file and return a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The data read from the CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def read_json_file(file_path):
    """
    Read a JSON file and return a pandas DataFrame.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        pandas.DataFrame: The data read from the JSON file.
    """
    data = pd.read_json(file_path)
    return data

# Read the CSV file
csv_file_path = '/Users/jose.monsalvo/project/numpy-pandas/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv'
data = read_csv_file(csv_file_path)
print(data)  # Print the data read from the CSV file

# Read the JSON file
json_file_path = '/Users/jose.monsalvo/project/numpy-pandas/hpcharactersdataraw.json'
data_json = read_json_file(json_file_path)
print(data_json)  # Print the data read from the JSON file

# Print the first 4 rows of the data
print(data[0:4])  # Print the first 4 rows of the data

# Print the 'Name' and 'Author' columns for the first 5 rows
print(data.loc[0:4, ['Name', 'Author']])  # Print the 'Name' and 'Author' columns for the first 5 rows

# Multiply the 'Reviews' column by -1
print(data.loc[:, ['Reviews']] * -1)  # Multiply the 'Reviews' column by -1

# Check if the 'Author' column is equal to 'JJ Smith'
cond = data.loc[:, ['Author']] == 'JJ Smith'
print(cond)  # Print the condition

# Print the first two columns of the data
print(data.iloc[:, 0:2])  # Print the first two columns of the data
