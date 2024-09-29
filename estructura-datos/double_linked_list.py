
class Node:
    def __init__(self, data, next=None):
        """
        Initializes a Node object with the given data and next pointer.

        Args:
            data: The data to be stored in the node.
            next: The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        """
        Initializes a TwoWayNode object with the given data, previous pointer, and next pointer.

        Args:
            data: The data to be stored in the node.
            previous: The previous node in the linked list. Defaults to None.
            next: The next node in the linked list. Defaults to None.
        """
        Node.__init__(self, data, next)
        self.previous = previous

class circleDoubleLinkedList():
    def __init__(self):
        """
        Initializes a circular doubly linked list.

        The circular doubly linked list is initialized with a head node and a tail node.
        The head and tail nodes are initially connected to each other to form a circular structure.
        The size of the linked list is set to 0.
        """
        self.head = TwoWayNode(None,None,None)
        self.tail = self.head
        self.size = 0

        self.head.next = self.tail
        self.head.previous = self.tail

    def range(self, start, stop):
        """
        Creates a circular doubly linked list with nodes containing values from start to stop-1.

        Args:
            start: The starting value of the range (inclusive).
            stop: The ending value of the range (exclusive).
        """
        self.head = TwoWayNode(start, next=None, previous=None)
        self.tail = self.head
        self.size = 1

        for data in range(start+1, stop):
            self.tail.next = TwoWayNode(data, previous=self.tail)
            self.tail = self.tail.next
            self.size += 1

        self.tail.next = self.head
        self.head.previous = self.tail

    def __str__(self):
        """
        Returns a string representation of the circular doubly linked list.

        Returns:
            A string representation of the circular doubly linked list.
        """
        probe = self.head
        result = ''
        while probe.next != self.head:
            result += f'{probe.data} '
            probe = probe.next
        result += f'{probe.data}'
        result = result.strip()
        return result

    def reverse(self):
        """
        Returns a string representation of the circular doubly linked list in reverse order.

        Returns:
            A string representation of the circular doubly linked list in reverse order.
        """
        probe = self.tail
        result = ''
        while probe.previous != self.tail:
            result += f'{probe.data} '
            probe = probe.previous
        result += f'{probe.data}'
        result = result.strip()
        return result

    def str_by_steps(self, steps, direction='forward'):
        """
        Returns a string representation of the circular doubly linked list by traversing a certain number of steps.

        Args:
            steps: The number of steps to traverse.
            direction: The direction of traversal. Can be 'forward' or 'backward'. Defaults to 'forward'.

        Returns:
            A string representation of the circular doubly linked list by traversing a certain number of steps.
        """
        result = ''

        if direction == 'forward':
            probe = self.head
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.next
                steps -= 1

        if direction == 'backward':
            probe = self.tail
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.previous
                steps -= 1

        result = result.strip()
        return result

    def search(self, target_item):
        """
        Searches for a target item in the circular doubly linked list.

        Args:
            target_item: The item to search for.

        Returns:
            The node containing the target item if found, -1 otherwise.
        """
        probe = self.head
        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            print(f'Target item {target_item} has been found')
            return probe
        else:
            print(f'Target item {target_item} is not in the linked list')
            return -1

    def replace(self, target_item, new_item):
        """
        Replaces a target item with a new item in the circular doubly linked list.

        Args:
            target_item: The item to be replaced.
            new_item: The new item to replace the target item.
        """
        probe = self.head

        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            probe.data = new_item
            print(f"{new_item} replaces the old value {target_item}")
        else:
            print(f"The target item {target_item} is not in the linked list")

    def unshift(self, new_item):
        """
        Inserts a new item/node at the beginning (head) of the circular doubly linked list.

        Args:
            new_item: The item to be inserted.
        """
        if self.size == 0:
            self.head.data = new_item
        else:
            self.head = TwoWayNode(new_item, previous=self.tail, next=self.head)
            self.head.next.previous = self.head
            self.tail.next = self.head
        self.size += 1

    def append(self, new_item):
        """
        Inserts a new item/node at the end (tail) of the circular doubly linked list.

        Args:
            new_item: The item to be inserted.
        """
        if self.size == 0:
            self.tail.data = new_item
        else:
            self.tail = TwoWayNode(new_item, previous=self.tail, next=self.head)
            self.tail.previous.next = self.tail
            self.head.previous = self.tail
        self.size += 1

    def shift(self):
        """
        Removes an item/node from the beginning (head) of the circular doubly linked list.

        Returns:
            The removed item if the list is not empty, None otherwise.
        """
        if self.size == 0:
            return None

        removed_item = self.head.data
        self.head = self.head.next

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def pop(self):
        """
        Removes an item/node from the end (tail) of the circular doubly linked list.

        Returns:
            The removed item if the list is not empty, None otherwise.
        """
        if self.size == 0:
            return None

        removed_item = self.tail.data
        self.tail = self.tail.previous

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def insert(self, new_item, index):
        """
        Inserts a new item/node at the specified index in the circular doubly linked list.

        Args:
            new_item: The item to be inserted.
            index: The index at which the item should be inserted.
        """
        if self.size == 0:
            self.head.data = new_item
            self.size += 1
        elif index <= 0:
            self.unshift(new_item)
        elif index >= self.size - 1:
            self.append(new_item)
        else:
            probe = self.head
            while index > 1 and probe.next != self.head:
                probe = probe.next
                index -= 1
            probe.next = TwoWayNode(new_item, previous=probe, next=probe.next)
            probe.next.next.previous = probe.next
            self.size += 1

    def delete_by_index(self, index):
        """
        Deletes an item/node at the specified index in the circular doubly linked list.

        Args:
            index: The index of the item to be deleted.

        Returns:
            The removed item if the list is not empty, None otherwise.
        """
        if self.size == 0:
            return None
        if index <= 0:
            self.shift()
        elif index >= self.size - 1:
            self.pop()
        else:
            probe = self.head
            while index > 1 and probe.next.next != self.head:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            probe.next.previous = probe
            self.size -= 1

            print(f'Removed_item: {removed_item}')
            return removed_item

    def clear(self):
        """
        Clears the circular doubly linked list by reinitializing it.
        """
        self.__init__()
