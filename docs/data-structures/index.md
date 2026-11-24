# Data structures in Python

A data structure is a way to organize data so operations such as lookup, insertion, deletion, and traversal are manageable.

The practical question is not "Can I implement this?" It is "Which representation makes this program simpler and efficient?"

## Practical mapping

| Abstract concept | Python choice | Typical use |
|---|---|---|
| Dynamic array | list | Ordered sequence, indexing, append |
| Stack | list | Last-in, first-out processing |
| Queue / deque | collections.deque | Work queues, both-end operations |
| Hash map | dict | Key-to-value lookup |
| Hash set | set | Uniqueness and membership |
| Priority queue | heapq | Repeatedly process smallest priority |
| Sorted sequence | bisect + list | Binary search and insertion positions |
| Graph | dict + list/set | Adjacency-list representation |

## Lists and dynamic arrays

Use a list when you need ordered values, fast index access, and efficient append at the end.

- Indexing: O(1).
- Append: amortized O(1).
- Insert or delete near the beginning: O(n).
- Membership search: O(n).

~~~python
tasks = ["read", "practice"]
tasks.append("review")
first_task = tasks[0]
~~~

## Stacks

A stack is last-in, first-out (LIFO). A Python list already supports the required operations efficiently:

~~~python
history = []
history.append("home")
history.append("profile")
current = history.pop()
~~~

append() pushes; pop() removes the most recently added item. Both are amortized O(1).

## Queues and deques

A queue is first-in, first-out (FIFO). Avoid repeatedly calling list.pop(0): removing the first list element shifts the remaining elements.

Use collections.deque:

~~~python
from collections import deque

jobs = deque(["compile", "test"])
jobs.append("package")
next_job = jobs.popleft()
~~~

Appending and removing from either end are O(1).

## Hash maps and sets

Python's dict and set are the practical hash-table tools.

~~~python
ages = {"Ada": 36, "Grace": 85}
ages["Linus"] = 56

seen_ids = {12, 18, 25}
already_seen = 18 in seen_ids
~~~

Lookup and membership are O(1) on average. Keys and set elements must be hashable. A hashable object's hash and equality behavior must remain stable while it is stored.

## Heaps and priority queues

Use heapq when you repeatedly need the smallest item. It operates on a regular list:

~~~python
import heapq

priorities = [7, 2, 5]
heapq.heapify(priorities)
heapq.heappush(priorities, 1)
next_priority = heapq.heappop(priorities)
~~~

Push and pop are O(log n); heapify is O(n); reading priorities[0] is O(1) when non-empty.

## Trees

A tree is a hierarchical structure. Python does not provide a general-purpose binary search tree in the standard library. Learn the tree invariants and traversals, then choose an appropriate representation for the task. For maintaining sorted positions in a list, bisect can help, but insertion into the middle of a list remains O(n).

## Graphs

A common representation is a dictionary mapping each vertex to its neighbors:

~~~python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
~~~

Use lists when neighbor order or repeated edges matter; use sets when fast membership and uniqueness matter. Breadth-first and depth-first search are covered in the algorithms section.

## When to implement from scratch

Implement a structure yourself only when you are studying its internals, working under a constraint that requires it, or evaluating a specialized design. For ordinary application code, prefer Python's tested built-ins and standard library.