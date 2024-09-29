from array import Array


class Grid:
    def __init__(self, rows, columns, fill_value=None):
        """
        Initializes a Grid object with the specified number of rows and columns.
        The optional fill_value parameter is used to initialize each element in the grid.
        """
        self.data = Array(rows)
        for i in range(rows):
            self.data[i] = Array(columns, fill_value)
    
    def get_height(self):
        """
        Returns the number of rows in the grid.
        """
        return len(self.data)
    
    def get_width(self):
        """
        Returns the number of columns in the grid.
        """
        return len(self.data[0])
    
    def __getitem__(self, index):
        """
        Returns the element at the specified index in the grid.
        """
        return self.data[index]
    
    def __str__(self):
        """
        Returns a string representation of the grid.
        """
        result = ''
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                result += str(self.data[i][j]) + ' '
            result += '\n'
        return result
    
if __name__ == '__main__':
    table = Grid(5, 5, 'papas')
    print(table)
    print(table.get_height())
    print(table.get_width())
    print(table[2][2])
    table[2][2] = 'papas fritas'
    print(table[2][2])
    print(table)
    print(table.get_height())
    print(table.get_width())
    classicArray = [[1,2], [3,4], [4,5], 6, 7]
    print(classicArray[1][0])