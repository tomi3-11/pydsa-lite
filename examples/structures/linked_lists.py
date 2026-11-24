from pydsa_lite.structures import DoublyLinkedList,SinglyLinkedList
singly=SinglyLinkedList([10,20]); singly.prepend(5); singly.append(30)
print("Singly:",list(singly)); singly.remove(20); print("After removal:",list(singly))
doubly=DoublyLinkedList(["a","b","c"])
print("Forward:",list(doubly)); print("Backward:",list(reversed(doubly)))
print("Removed tail:",doubly.pop_back())
