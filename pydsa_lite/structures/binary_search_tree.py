"""A binary search tree for values that can be ordered."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.left: _Node[T] | None = None
        self.right: _Node[T] | None = None


class BinarySearchTree(Generic[T]):
    """A set-like binary search tree with unique values.

    Values smaller than a node go left; larger values go right. Duplicate
    insertions are ignored. Operations are O(log n) on a balanced tree and
    O(n) in the worst case when insertion order creates a chain.
    """

    def __init__(self) -> None:
        self._root: _Node[T] | None = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Yield values in ascending order (in-order traversal)."""
        yield from self._inorder(self._root)

    def _inorder(self, node: _Node[T] | None) -> Iterator[T]:
        if node is not None:
            yield from self._inorder(node.left)
            yield node.value
            yield from self._inorder(node.right)

    def insert(self, value: T) -> bool:
        """Insert value; return False if an equal value already exists."""
        if self._root is None:
            self._root = _Node(value)
            self._size = 1
            return True

        current = self._root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = _Node(value)
                    self._size += 1
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = _Node(value)
                    self._size += 1
                    return True
                current = current.right

    def __contains__(self, value: object) -> bool:
        try:
            self.find(value)  # type: ignore[arg-type]
        except KeyError:
            return False
        return True

    def find(self, value: T) -> T:
        """Return the stored value, raising KeyError when it is absent."""
        current = self._root
        while current is not None:
            if value == current.value:
                return current.value
            current = current.left if value < current.value else current.right
        raise KeyError(value)

    def remove(self, value: T) -> None:
        """Remove value while preserving the search-tree ordering invariant."""
        self._root = self._remove(self._root, value)

    def _remove(self, node: _Node[T] | None, value: T) -> _Node[T] | None:
        if node is None:
            raise KeyError(value)
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            self._size -= 1
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.right = self._remove_successor(node.right)
        return node

    def _remove_successor(self, node: _Node[T]) -> _Node[T] | None:
        if node.left is None:
            return node.right
        node.left = self._remove_successor(node.left)
        return node
