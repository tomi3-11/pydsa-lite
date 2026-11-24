# Linked lists

A linked list stores values in nodes. Each node contains a value and a
reference to another node. Nodes do not need to be adjacent in memory.

## Singly linked list

A singly linked node points forward. The list tracks its head; reaching a
later node requires following links one at a time.

~~~python
from pydsa_lite.structures import SinglyLinkedList
numbers = SinglyLinkedList([10, 20])
numbers.prepend(5)
numbers.append(30)
print(list(numbers))  # [5, 10, 20, 30]
numbers.remove(20)
~~~

## Doubly linked list

A doubly linked node points forward and backward. The implementation tracks
both head and tail, making insertion and removal at either end O(1).

~~~python
from pydsa_lite.structures import DoublyLinkedList
letters = DoublyLinkedList(["a", "b", "c"])
print(list(letters))
print(list(reversed(letters)))
letters.pop_back()
~~~

## Complexity

| Operation | Singly linked | Doubly linked |
|---|---:|---:|
| Search | O(n) | O(n) |
| Prepend | O(1) | O(1) |
| Append | O(n) | O(1) |
| Remove first | O(1) | O(1) |
| Remove last | Not provided | O(1) |
| Remove by value | O(n) | O(n) |
| Length | O(1) | O(1) |
| Space | O(n) | O(n) |

The doubly linked node uses extra memory for its backward reference.

## Invariants

- An empty list has no head; a doubly linked list also has no tail.
- The head of a singly linked list is the first node.
- In a doubly linked list, head has no previous node and tail has no next.
- The stored size equals the number of reachable nodes.

Run: python examples/structures/linked_lists.py
