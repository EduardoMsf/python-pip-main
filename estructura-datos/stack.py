from node import Node

class Stack:
    """
    A class representing a stack data structure.

    Attributes:
    - top: The top node of the stack.
    - size: The number of elements in the stack.

    Methods:
    - push(data): Adds an element to the top of the stack.
    - pop(): Removes and returns the element from the top of the stack.
    - peek(): Returns the element from the top of the stack without removing it.
    - clear(): Removes all elements from the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Adds an element to the top of the stack.

        Parameters:
        - data: The data to be added to the stack.
        """
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1
    
    def pop(self):
        """
        Removes and returns the element from the top of the stack.

        Returns:
        - The element removed from the top of the stack.

        Raises:
        - "Stack is empty." if the stack is empty.
        """
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            
            return data
        else:
            return "Stack is empty."
    
    def peek(self):
        """
        Returns the element from the top of the stack without removing it.

        Returns:
        - The element from the top of the stack.

        Raises:
        - "Stack is empty." if the stack is empty.
        """
        if self.top:
            return self.top.data
        else:
            return "Stack is empty."
        
    def clear(self):
        """
        Removes all elements from the stack.
        """
        while self.top:
            self.pop()

#
class Stack2:
    def __init__(self):
        self.top = None
        self.size = 0


    def push(self, data):
        node = Node(data, self.top)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1


    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return ("The stack is empty")


    def peek(self):
        return self.top.data if self.top else ("The stack is empty")


    def clear(self):
        while self.top:
            self.pop()


    def search_element(self, data):
        if self.top:
            current = self.top
            while current:
                if current.data == data:
                    return (f'Elemet {data} founded')
                current = current.next
            return (f'Elemet {data} not founded')
#