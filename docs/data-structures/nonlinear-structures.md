# Non-linear data structures

## Hash table

A hash table maps keys to values. It hashes a key to choose a bucket. When
different keys choose the same bucket, separate chaining stores both entries
in that bucket. This implementation grows its bucket array above a 0.75 load
factor.

| Operation | Average | Worst |
|---|---:|---:|
| Lookup | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Keys must be hashable. Assigning an existing key replaces its value; reading
or deleting a missing key raises KeyError.

## Binary search tree

For every node, values in its left subtree are smaller and values in its right
subtree are larger. Duplicate insertions are ignored. Iteration performs an
in-order traversal, producing ascending values.

| Operation | Balanced | Worst |
|---|---:|---:|
| Search / insert / remove | O(log n) | O(n) |
| In-order traversal | O(n) | O(n) |

This is an ordinary, unbalanced BST. Sorted insertion can make it behave like
a linked list; self-balancing trees are outside this milestone.

## Min-heap

A min-heap is a complete binary tree represented by an array. Every parent is
less than or equal to its children, so the smallest value is at index zero.
For an element at index i, its children are at 2*i + 1 and 2*i + 2.

| Operation | Complexity |
|---|---:|
| Peek minimum | O(1) |
| Insert / remove minimum | O(log n) |
| Build from values | O(n) |

Iteration exposes the internal heap-array order, not sorted order. Repeatedly
calling pop() produces values in ascending order.

## Graph

A graph stores vertices and edges. This implementation uses an adjacency list:
each vertex maps to its outgoing neighbors and edge weights. Graphs are
undirected by default; pass directed=True for directed edges. Adding an edge
automatically creates missing endpoint vertices.

| Operation | Complexity |
|---|---:|
| Add vertex | O(1) average |
| Add edge | O(1) average |
| List neighbors | O(degree) |
| Remove vertex | O(V + E) |

The graph stores numeric edge weights. Traversal and shortest-path algorithms
are covered in a later milestone.

## Runnable examples

Run these after installing the project in editable mode:

- python examples/structures/hash_table.py
- python examples/structures/binary_search_tree.py
- python examples/structures/min_heap.py
- python examples/structures/graph.py
