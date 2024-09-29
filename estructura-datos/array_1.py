
class Array:
    """
    A class representing an array.

    Args:
    - capacity (int): The capacity of the array.
    - fill_value (optional): The value to fill the array with. Defaults to None.

    Attributes:
    - items (list): The list to store the elements of the array.

    Methods:
    - __init__(self, capacity, fill_value=None): Initializes the array with the given capacity and fill value.
    - __len__(self): Returns the number of elements in the array.
    - __str__(self): Returns a string representation of the array.
    - __iter__(self): Returns an iterator object for the array.
    - __getitem__(self, index): Returns the element at the given index.
    - __setitem__(self, index, new_item): Sets the element at the given index to the new item.
    """

    def __init__(self, capacity, fill_value=None): 
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item



if __name__ == '__main__':
    menu = Array(5)
    print(menu.__len__())
    print(menu)
    for item in menu:
        print(item)
    menu[2] = 'papas'
    print(menu[2])
    print(menu)
    print(menu.__len__())
    print(len(menu))