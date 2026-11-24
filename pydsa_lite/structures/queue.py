"""A linked-node first-in, first-out (FIFO) queue."""

from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    """One queue node, pointing to the next value in line."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional[_Node[T]] = None


class Queue(Generic[T]):
    """A queue where the earliest enqueued value leaves first.

    The queue tracks both its front and rear nodes. Enqueue, dequeue, and
    peek all take O(1) time. Iteration follows dequeue order.
    """

    def __init__(self) -> None:
        self._front: Optional[_Node[T]] = None
        self._rear: Optional[_Node[T]] = None
        self._size = 0

    def __len__(self) -> int:
        """Return the number of values in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Yield values from front to rear."""
        current = self._front
        while current is not None:
            yield current.value
            current = current.next

    def is_empty(self) -> bool:
        """Return True when the queue contains no values."""
        return self._size == 0

    def enqueue(self, value: T) -> None:
        """Add a value to the rear in O(1) time."""
        new_node = _Node(value)

        if self._rear is None:
            # An empty queue has no front or rear node.
            self._front = new_node
        else:
            self._rear.next = new_node

        self._rear = new_node
        self._size += 1

    def dequeue(self) -> T:
        """Remove and return the front value in O(1) time.

        Raises:
            IndexError: If the queue is empty.
        """
        if self._front is None:
            raise IndexError("dequeue from empty queue")

        value = self._front.value
        self._front = self._front.next

        if self._front is None:
            # Removing the final node makes both ends empty.
            self._rear = None

        self._size -= 1
        return value

    def peek(self) -> T:
        """Return the front value without removing it in O(1) time.

        Raises:
            IndexError: If the queue is empty.
        """
        if self._front is None:
            raise IndexError("peek at empty queue")
        return self._front.value
