"""Singly and doubly linked lists for learning node-based structures.

The node classes are private implementation details. Public list methods
provide a small, predictable API and maintain the node-link invariants.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class _SinglyNode(Generic[T]):
    """A node that stores a value and a link to the next node."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional[_SinglyNode[T]] = None


class SinglyLinkedList(Generic[T]):
    """A forward-only chain of nodes.

    The list stores its head and size. Prepending and removing the first
    element take O(1) time. Appending, searching, and removing by value take
    O(n) time because the list may need to be traversed.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._head: Optional[_SinglyNode[T]] = None
        self._size = 0

        if values is not None:
            for value in values:
                self.append(value)

    def __len__(self) -> int:
        """Return the number of values in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Yield values from the head toward the tail."""
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)!r})"

    def is_empty(self) -> bool:
        """Return True when the list has no nodes."""
        return self._size == 0

    def prepend(self, value: T) -> None:
        """Insert a value at the head in O(1) time."""
        new_node = _SinglyNode(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def append(self, value: T) -> None:
        """Insert a value at the tail in O(n) time."""
        new_node = _SinglyNode(value)

        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._size += 1

    def find(self, value: T) -> bool:
        """Return whether value occurs in the list; O(n) time."""
        return any(item == value for item in self)

    def remove(self, value: T) -> None:
        """Remove the first matching value.

        Raises:
            ValueError: If the value is not present.
        """
        previous: Optional[_SinglyNode[T]] = None
        current = self._head

        while current is not None:
            if current.value == value:
                if previous is None:
                    # The matching node is the head.
                    self._head = current.next
                else:
                    # Skip the matching node in the chain.
                    previous.next = current.next

                self._size -= 1
                return

            previous = current
            current = current.next

        raise ValueError(f"{value!r} is not in the list")

    def pop_front(self) -> T:
        """Remove and return the head in O(1) time.

        Raises:
            IndexError: If the list is empty.
        """
        if self._head is None:
            raise IndexError("pop from empty linked list")

        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value


class _DoublyNode(Generic[T]):
    """A node with links to both its previous and next neighbors."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.previous: Optional[_DoublyNode[T]] = None
        self.next: Optional[_DoublyNode[T]] = None


class DoublyLinkedList(Generic[T]):
    """A two-way node chain with references to both ends.

    Tracking the head and tail makes insertion and removal at either end
    O(1). Searching for a value or removing by value takes O(n) time.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._head: Optional[_DoublyNode[T]] = None
        self._tail: Optional[_DoublyNode[T]] = None
        self._size = 0

        if values is not None:
            for value in values:
                self.append(value)

    def __len__(self) -> int:
        """Return the number of values in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Yield values from head to tail."""
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __reversed__(self) -> Iterator[T]:
        """Yield values from tail to head."""
        current = self._tail
        while current is not None:
            yield current.value
            current = current.previous

    def __repr__(self) -> str:
        return f"DoublyLinkedList({list(self)!r})"

    def is_empty(self) -> bool:
        """Return True when the list has no nodes."""
        return self._size == 0

    def prepend(self, value: T) -> None:
        """Insert a value at the head in O(1) time."""
        new_node = _DoublyNode(value)
        new_node.next = self._head

        if self._head is None:
            # The new node is both the head and the tail.
            self._tail = new_node
        else:
            self._head.previous = new_node

        self._head = new_node
        self._size += 1

    def append(self, value: T) -> None:
        """Insert a value at the tail in O(1) time."""
        new_node = _DoublyNode(value)
        new_node.previous = self._tail

        if self._tail is None:
            # The new node is both the head and the tail.
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1

    def find(self, value: T) -> bool:
        """Return whether value occurs in the list; O(n) time."""
        return any(item == value for item in self)

    def remove(self, value: T) -> None:
        """Remove the first matching value and reconnect its neighbors.

        Raises:
            ValueError: If the value is not present.
        """
        current = self._head

        while current is not None:
            if current.value == value:
                if current.previous is None:
                    self._head = current.next
                else:
                    current.previous.next = current.next

                if current.next is None:
                    self._tail = current.previous
                else:
                    current.next.previous = current.previous

                self._size -= 1
                return

            current = current.next

        raise ValueError(f"{value!r} is not in the list")

    def pop_front(self) -> T:
        """Remove and return the head in O(1) time.

        Raises:
            IndexError: If the list is empty.
        """
        if self._head is None:
            raise IndexError("pop from empty linked list")

        value = self._head.value
        self._head = self._head.next

        if self._head is None:
            self._tail = None
        else:
            self._head.previous = None

        self._size -= 1
        return value

    def pop_back(self) -> T:
        """Remove and return the tail in O(1) time.

        Raises:
            IndexError: If the list is empty.
        """
        if self._tail is None:
            raise IndexError("pop from empty linked list")

        value = self._tail.value
        self._tail = self._tail.previous

        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None

        self._size -= 1
        return value
