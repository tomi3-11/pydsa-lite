"""An array-backed min-heap."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    """A min-heap where the smallest value is always at the root.

    Parent/child relationships are stored in an array. Push and pop are
    O(log n), while peek is O(1). Values must be mutually comparable.
    """

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._items = list(values)
        for index in range(len(self._items) // 2 - 1, -1, -1):
            self._sift_down(index)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        """Iterate over the internal heap array (not sorted order)."""
        return iter(self._items.copy())

    def push(self, value: T) -> None:
        """Add a value and restore the heap invariant."""
        self._items.append(value)
        self._sift_up(len(self._items) - 1)

    def peek(self) -> T:
        """Return the smallest value without removing it."""
        if not self._items:
            raise IndexError("peek from empty heap")
        return self._items[0]

    def pop(self) -> T:
        """Remove and return the smallest value."""
        if not self._items:
            raise IndexError("pop from empty heap")
        if len(self._items) == 1:
            return self._items.pop()

        smallest = self._items[0]
        self._items[0] = self._items.pop()
        self._sift_down(0)
        return smallest

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent] <= self._items[index]:
                break
            self._items[parent], self._items[index] = (
                self._items[index], self._items[parent]
            )
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._items)
        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index
            if left < size and self._items[left] < self._items[smallest]:
                smallest = left
            if right < size and self._items[right] < self._items[smallest]:
                smallest = right
            if smallest == index:
                return
            self._items[index], self._items[smallest] = (
                self._items[smallest], self._items[index]
            )
            index = smallest
