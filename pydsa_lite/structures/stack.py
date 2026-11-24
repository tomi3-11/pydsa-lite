"""A linked-node last-in, first-out (LIFO) stack."""

from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    """One stack node, pointing to the node below it."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional[_Node[T]] = None


class Stack(Generic[T]):
    """A stack where the most recently pushed value leaves first.

    The top reference points to the newest node. Push, pop, and peek all
    take O(1) time. Iteration visits values from top to bottom.
    """

    def __init__(self) -> None:
        self._top: Optional[_Node[T]] = None
        self._size = 0

    def __len__(self) -> int:
        """Return the number of values in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Yield values from the top of the stack downward."""
        current = self._top
        while current is not None:
            yield current.value
            current = current.next

    def is_empty(self) -> bool:
        """Return True when the stack contains no values."""
        return self._size == 0

    def push(self, value: T) -> None:
        """Place a value on top of the stack in O(1) time."""
        new_node = _Node(value)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self) -> T:
        """Remove and return the top value in O(1) time.

        Raises:
            IndexError: If the stack is empty.
        """
        if self._top is None:
            raise IndexError("pop from empty stack")

        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self) -> T:
        """Return the top value without removing it in O(1) time.

        Raises:
            IndexError: If the stack is empty.
        """
        if self._top is None:
            raise IndexError("peek at empty stack")
        return self._top.value
