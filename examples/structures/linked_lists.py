"""Demonstrate singly and doubly linked list operations.

Run after installing the project in editable mode:
    python examples/structures/linked_lists.py
"""

from pydsa_lite.structures import DoublyLinkedList, SinglyLinkedList

# A singly linked list can grow at either end.
singly = SinglyLinkedList([10, 20])
singly.prepend(5)
singly.append(30)
print("Singly linked:", list(singly))

singly.remove(20)
print("After removing 20:", list(singly))

# A doubly linked list can also be traversed in reverse.
doubly = DoublyLinkedList(["a", "b", "c"])
print("Forward:", list(doubly))
print("Backward:", list(reversed(doubly)))
print("Removed from tail:", doubly.pop_back())
