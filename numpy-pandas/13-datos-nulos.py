import pandas as pd 
import numpy as np 

def analyze_missing_data():
    """
    Analyzes missing data in a pandas DataFrame.

    This function demonstrates various techniques to handle missing data in a DataFrame.

    Returns:
        None
    """

    # Create a dictionary with some missing values
    dict = {'Col1': [1, 2, 3, np.nan], 'Col2': [4, np.nan, 6, 7], 'Col3': ['a', 'b', 'c', None]}
    print(dict)

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(dict)
    print(df)

    # Check for missing values in the DataFrame
    print(df.isnull())

    # Convert missing values to 1 and non-missing values to 0
    print(df.isnull()*1)

    # Uncomment the following line to fill missing values with 'Missing'
    # df.fillna('Missing', inplace=True)
    print(df)

    # Uncomment the following line to fill missing values with the mean of the column
    # print(df.fillna(df.mean()))

    # Convert 'Col1' and 'Col2' columns to numeric type, replacing non-numeric values with NaN
    df['Col1'] = pd.to_numeric(df['Col1'], errors='coerce')
    df['Col2'] = pd.to_numeric(df['Col2'], errors='coerce')
    print(df.dtypes)

    # Interpolate missing values using linear interpolation
    print(df.interpolate())

    # Drop rows with missing values
    df.dropna(inplace=True)
    print(df)

# Call the function to analyze missing data
analyze_missing_data()
