# Stacks and queues

Both structures restrict the order in which values leave a collection.

## Stack: last in, first out

A stack (LIFO) removes the newest value first. Think of a stack of plates:
you place a plate on top and take the top plate off first.

~~~python
from pydsa_lite.structures import Stack
stack = Stack()
stack.push("first")
stack.push("second")
print(stack.pop())  # second
print(stack.peek())  # first
~~~

Stacks are useful for undo history, function-call tracking, and depth-first
search.

## Queue: first in, first out

A queue (FIFO) removes the oldest value first. Think of a line: the first
person to join is the first person served.

~~~python
from pydsa_lite.structures import Queue
queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
print(queue.dequeue())  # first
print(queue.peek())  # second
~~~

Queues are useful for task scheduling, request processing, and breadth-first
search.

## Complexity

| Operation | Stack | Queue |
|---|---:|---:|
| Insert | O(1) push | O(1) enqueue |
| Remove | O(1) pop | O(1) dequeue |
| Inspect next value | O(1) peek | O(1) peek |
| Length | O(1) | O(1) |
| Space | O(n) | O(n) |

The queue tracks both front and rear nodes, so enqueue does not traverse the
structure. Empty removal or inspection raises IndexError.

Run python examples/structures/stack.py and
python examples/structures/queue.py to try the examples.
