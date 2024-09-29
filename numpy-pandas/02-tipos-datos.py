import numpy as np

def convert_array_data_types():
    """
    This function demonstrates how to convert the data type of a NumPy array.
    It creates an array of numbers and converts it to different data types.
    """
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='float64')
    
    print(arr.dtype)
    print(arr)
    
    arr_int = arr.astype(int)
    """np.int32 or np.int64 and np.float32 or np.float64 and np.string_ and np.unicode_ and np.bool_
    """
    print(arr_int.dtype)
    print(arr_int)
    
    arr_str = arr.astype(str)
    print(arr_str.dtype)
    print(arr_str)

if __name__ == "__main__":
    convert_array_data_types()
