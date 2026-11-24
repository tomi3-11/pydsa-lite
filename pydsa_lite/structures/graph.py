"""A weighted graph stored as an adjacency list."""

from __future__ import annotations

from collections.abc import Hashable, Iterator
from typing import Generic, TypeVar

V = TypeVar("V", bound=Hashable)


class Graph(Generic[V]):
    """A weighted directed or undirected graph.

    Each vertex maps to its outgoing neighbors and edge weights. Graphs are
    undirected by default. Adding an edge creates missing endpoint vertices.
    Neighbor lookup is O(degree); adding a vertex is O(1) on average.
    """

    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self._adjacency: dict[V, dict[V, float]] = {}

    def __len__(self) -> int:
        return len(self._adjacency)

    def __iter__(self) -> Iterator[V]:
        return iter(self._adjacency)

    def add_vertex(self, vertex: V) -> None:
        """Add a vertex if it does not already exist."""
        self._adjacency.setdefault(vertex, {})

    def add_edge(self, source: V, target: V, weight: float = 1) -> None:
        """Add an edge, creating endpoints when necessary."""
        self.add_vertex(source)
        self.add_vertex(target)
        self._adjacency[source][target] = weight
        if not self.directed:
            self._adjacency[target][source] = weight

    def remove_edge(self, source: V, target: V) -> None:
        """Remove an edge; raise KeyError if it does not exist."""
        if source not in self._adjacency or target not in self._adjacency[source]:
            raise KeyError((source, target))
        del self._adjacency[source][target]
        if not self.directed:
            del self._adjacency[target][source]

    def remove_vertex(self, vertex: V) -> None:
        """Remove a vertex and all edges pointing to or from it."""
        if vertex not in self._adjacency:
            raise KeyError(vertex)
        del self._adjacency[vertex]
        for neighbors in self._adjacency.values():
            neighbors.pop(vertex, None)

    def has_edge(self, source: V, target: V) -> bool:
        """Return whether source has an edge to target."""
        return source in self._adjacency and target in self._adjacency[source]

    def neighbors(self, vertex: V) -> tuple[V, ...]:
        """Return the outgoing neighbors in insertion order."""
        if vertex not in self._adjacency:
            raise KeyError(vertex)
        return tuple(self._adjacency[vertex])

    def edge_weight(self, source: V, target: V) -> float:
        """Return an edge's weight, raising KeyError when no edge exists."""
        try:
            return self._adjacency[source][target]
        except KeyError:
            raise KeyError((source, target)) from None

    def degree(self, vertex: V) -> int:
        """Return the outgoing degree (degree for undirected graphs)."""
        if vertex not in self._adjacency:
            raise KeyError(vertex)
        return len(self._adjacency[vertex])
