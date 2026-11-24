# Algorithms

An algorithm is a repeatable method for solving a problem. A good solution is correct, understandable, and appropriate for the input constraints.

## Search

- Linear search checks items one by one: O(n).
- Binary search repeatedly halves a sorted search space: O(log n).
- Python's in operator is appropriate for many everyday membership checks; use bisect when you need insertion points in sorted sequences.

## Sorting

Use sorted(iterable, key=..., reverse=...) when you need a new sorted list. Use list.sort() when you can mutate the list in place.

~~~python
users = [
    {"name": "Ada", "score": 91},
    {"name": "Grace", "score": 98},
]
ranked = sorted(users, key=lambda user: user["score"], reverse=True)
~~~

Python's sort is stable. In normal application code, use the built-in sort rather than implementing a sorting algorithm yourself. Implement sorting algorithms as exercises to understand partitioning, merging, and complexity.

## Common problem-solving patterns

- Two pointers: coordinate two positions in a sequence.
- Sliding window: maintain information about a moving contiguous range.
- Prefix sums: answer range-sum queries efficiently.
- Recursion: express a problem in terms of smaller instances.
- Divide and conquer: split, solve, and combine.
- Greedy: make a locally optimal choice when a proof supports it.
- Dynamic programming: reuse results of overlapping subproblems.

## Graph algorithms

Learn breadth-first search (BFS), depth-first search (DFS), topological ordering, and shortest paths. Represent graphs with standard Python collections before considering specialized libraries.

## Learning rule

For every algorithm, document:
1. The problem it solves.
2. The key observation or invariant.
3. A worked example.
4. A readable implementation.
5. Time and auxiliary-space complexity.
6. Edge cases and tests.