from node import Node


class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.tail = None
        self.size = 0

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Parameters:
        - data: The data to be stored in the new node.
        """
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def size(self):
        """
        Returns the number of nodes in the linked list.

        Returns:
        - The size of the linked list.
        """
        return str(self.size)

    def iter(self):
        """
        Returns a generator that iterates over the data of each node in the linked list.

        Yields:
        - The data of each node in the linked list.
        """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """
        Deletes the first occurrence of a node with the given data from the linked list.

        Parameters:
        - data: The data to be deleted.

        Returns:
        - The data of the deleted node, or None if the data was not found.
        """
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if previous:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            previous = current
            current = current.next

    def search(self, data):
        """
        Searches for a node with the given data in the linked list.

        Parameters:
        - data: The data to search for.

        Prints:
        - "Data {data} found" if the data is found in the linked list.
        - "Data {data} not found" if the data is not found in the linked list.
        """
        for node in self.iter():
            if data == node:
                print(f'Data {data} found') 
                return 
        print(f'Data {data} not found')

    def clear(self):
        """
        Clears the linked list by setting the tail to None and the size to 0.
        """
        self.tail = None
        self.size = 0

if __name__ == '__main__':
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')
    current = words.tail
    while current:
        print(current.data)
        current = current.next
    
    for word in words.iter():
        print(word)

    words.search('spam')
    words.clear()
    print(words.size)

    arr = [1,2,3,4,5]
    arrToLinkedList = SinglyLinkedList()
    for i in arr:
        arrToLinkedList.append(i)
    for i in arrToLinkedList.iter():
        print(i)
    print(arrToLinkedList)





class SinglyLinkedList2:
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None
        self.size = 0 

    def add_to_start(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Parameters:
        - data: The data to be stored in the new node.
        """
        self.head = Node(data, self.head)
        print(f"Nodo {self.head.data} añadido a la cabezera.")
        self.size += 1

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Parameters:
        - data: The data to be stored in the new node.
        """
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
        print(f"Nodo {node.data} añadido a la cola.")
        self.size += 1

    def insert(self, data, index):
        """
        Inserts a new node with the given data at the specified index in the linked list.

        Parameters:
        - data: The data to be stored in the new node.
        - index: The index at which to insert the new node.
        """
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None or index <= 0:
                self.head = Node(data, self.head)
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next != None:
                    probe = probe.next
                    index -= 1
                probe.next = Node(data, probe.next)
            print(f"Nodo {data} añadido.")
            self.size += 1

    def replace(self, data, new_data):
        """
        Replaces the data of the first occurrence of a node with the given data in the linked list.

        Parameters:
        - data: The data to be replaced.
        - new_data: The new data to be stored in the node.
        """
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = new_data
            print(f"El nodo {data} ha sido reemplazado por {new_data}")
        else:
            print(f"The target item {data} is not in the linked list")

    def delete(self, index):
        """
        Deletes the node at the specified index in the linked list.

        Parameters:
        - index: The index of the node to be deleted.
        """
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None:
                print("No hay nodos que eliminar.")
            elif self.head.next is None:
                print(f"Nodo: {self.head.data} eliminado.")
                self.head = None
                self.size -= 1
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next.next != None:
                    probe = probe.next
                    index -= 1
                removed_item = probe.next.data
                probe.next = probe.next.next
                print(f"Nodo:{removed_item} eliminado.")
                self.size -= 1

    def pop(self):
        """
        Deletes the last node in the linked list.
        """
        data = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            data = probe.next.data
            probe.next = None
        self.size -= 1
        print(f"Ultimo nodo {data} eliminado.")

    def search(self, data):
        """
        Searches for a node with the given data in the linked list.

        Parameters:
        - data: The data to search for.

        Prints:
        - "El nodo {data} ha sido encontrado." if the data is found in the linked list.
        - "El nodo {data} no se encuentra en el grafo." if the data is not found in the linked list.
        """
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            print(f"El nodo {data} ha sido encontrado.")
            return probe
        else:
            print(f"El nodo {data} no se encuentra en el grafo.")

    def count_nodes(self):
        """
        Returns the number of nodes in the linked list.

        Returns:
        - The size of the linked list.
        """
        return self.size

    def print(self):
        """
        Prints the data of each node in the linked list.
        """
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    
    def clear(self):
        """
        Clears the linked list by setting the head to None and the size to 0.
        """
        self.head = None
        self.size = 0