"""A small hash table using separate chaining for collision handling."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar, cast

K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V]):
    """A hash table mapping unique keys to values.

    Collisions are stored in per-bucket lists (separate chaining). The table
    grows when its load factor exceeds 0.75. Lookup, insertion, and deletion
    are O(1) on average and O(n) in the worst case.
    """

    _MAX_LOAD = 0.75

    def __init__(self, initial_capacity: int = 8) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be at least 1")
        capacity = 1
        while capacity < initial_capacity:
            capacity *= 2
        self._buckets: list[list[tuple[K, V]]] = [[] for _ in range(capacity)]
        self._size = 0

    def __len__(self) -> int:
        """Return the number of key-value pairs in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[K]:
        """Iterate over keys in bucket order."""
        for bucket in self._buckets:
            for key, _ in bucket:
                yield key

    def __contains__(self, key: object) -> bool:
        """Return whether key exists in the table."""
        try:
            self[key]  # type: ignore[index]
        except KeyError:
            return False
        return True

    def __getitem__(self, key: K) -> V:
        """Return a value by key, raising KeyError when absent."""
        bucket = self._buckets[self._index(key)]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        raise KeyError(key)

    def __setitem__(self, key: K, value: V) -> None:
        """Insert or replace a value. Replacing a key does not grow the table."""
        index = self._index(key)
        bucket = self._buckets[index]
        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[position] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1
        if self._size / len(self._buckets) > self._MAX_LOAD:
            self._resize()

    def __delitem__(self, key: K) -> None:
        """Delete a key, raising KeyError when it is absent."""
        bucket = self._buckets[self._index(key)]
        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[position]
                self._size -= 1
                return
        raise KeyError(key)

    def get(self, key: K, default: V | None = None) -> V | None:
        """Return the value for key, or default when key is absent."""
        try:
            return self[key]
        except KeyError:
            return default

    def _index(self, key: K) -> int:
        return hash(key) % len(self._buckets)

    def _resize(self) -> None:
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._buckets[self._index(key)].append((key, value))
