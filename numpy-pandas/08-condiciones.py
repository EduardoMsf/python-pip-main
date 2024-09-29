import numpy as np 

def apply_conditions():
    """
    This script demonstrates the use of conditions in NumPy arrays.

    It creates a NumPy array, applies conditions to filter the array, and modifies the array based on the conditions.

    Steps:
    1. Create a NumPy array using `np.linspace` function.
    2. Print the original array.
    3. Print the result of the condition `arr > 5`, which returns a boolean array.
    4. Create a new array `indices_condicion` by applying multiple conditions using logical operators.
    5. Print the elements of `arr` that satisfy the conditions `indices_condicion` and `(arr < 9)`.
    6. Modify the elements of `arr` that satisfy the condition `arr > 5` and set them to 99.
    7. Print the modified array.

    Returns:
    None
    """
    arr = np.linspace(1,10,10, dtype='int8')
    print(arr)
    print(arr > 5)

    indices_condicion = arr > 5

    print(arr[indices_condicion & (arr < 9)])
    arr[arr > 5] = 99
    print(arr)

apply_conditions()
