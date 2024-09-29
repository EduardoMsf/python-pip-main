from typing import Optional, Any
from node import Node

class CicularLinkedList:
    """
    Represents a circular linked list data structure.

    Attributes:
        _head (Optional[Node]): The head node of the circular linked list.
        _size (int): The size of the circular linked list.

    Methods:
        __init__(*items): Initializes the circular linked list with optional items.
        size() -> int: Returns the size of the circular linked list.
        append(item: Any) -> None: Appends an item to the end of the list.
        iter() -> Iterator: Iterates through the circular linked list.
        iternodes() -> Iterator: Iterates through the circular linked list nodes.
        __iter__() -> Iterator: Returns an iterator for the circular linked list.
        __len__() -> int: Returns the size of the circular linked list.
        __str__() -> str: Returns a string representation of the circular linked list.
    """

    _head: Optional[Node] = None
    _size: int = 0

    def __init__(self, *items):
        """Initializes the circular linked list with optional items."""
        self._head = None
        self._size = 0

        for item in items:
            self.append(item)

    def size(self) -> int:
        """Returns the size of the circular linked list."""
        return self._size

    def append(self, item: Any) -> None:
        """Appends an item to the end of the list.

        Time complexity: O(n)
        """
        if self._head is None:
            self._head = Node(item)
            self._head.next = self._head
        else:
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = Node(item)
            current.next.next = self._head

        self._size += 1

    def iter(self):
        """Iterates through the circular linked list."""
        current = self._head
        while current.next != self._head:
            value = current.value
            current = current.next
            yield value
        yield current

    def iternodes(self):
        """Iterates through the circular linked list nodes."""
        current = self._head
        while current.next != self._head:
            yield current
            current = current.next
        yield current

    def __iter__(self):
        """Returns an iterator for the circular linked list."""
        return self.iter()

    def __len__(self) -> int:
        """Returns the size of the circular linked list."""
        return self._size

    def __str__(self) -> str:
        """Returns a string representation of the circular linked list."""
        list_items = list(self.iter())
        return ' -> '.join(str(item) for item in list_items)


if __name__ == '__main__':
    import unittest

    class CircularLinkedListTestCase(unittest.TestCase):
        """
        Test case for the CircularLinkedList class.
        """

        def test_initialize_empty(self):
            """Test case for initializing an empty circular linked list."""
            self.assertEqual(len(CicularLinkedList()), 0)

        def test_initialize_with_items(self):
            """Test case for initializing a circular linked list with items."""
            self.assertEqual(len(CicularLinkedList(1, 2, 3)), 3)

        def test_append(self):
            """Test case for appending items to the circular linked list."""
            cll = CicularLinkedList()
            cll.append(1)
            cll.append(2)
            cll.append(3)
            self.assertEqual(len(cll), 3)

        def test_iter(self):
            """Test case for iterating through the circular linked list."""
            cll = CicularLinkedList(1, 2, 3)
            self.assertEqual(list(cll), [1, 2, 3])

        def test_first_node_linked_with_last_node(self):
            """Test case for checking if the first node is linked with the last node."""
            cll = CicularLinkedList(1, 2, 3)
            head = cll._head
            for item in cll.iternodes():
                pass
            self.assertIs(head, item.next)

    unittest.main(verbosity=2)