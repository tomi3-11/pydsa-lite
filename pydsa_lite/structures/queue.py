"""A first-in, first-out queue."""
from __future__ import annotations
from typing import Generic,Iterator,Optional,TypeVar
T=TypeVar("T")
class _Node(Generic[T]):
    def __init__(self,value:T)->None:self.value=value; self.next:Optional[_Node[T]]=None
class Queue(Generic[T]):
    """Linked-node FIFO queue; enqueue, dequeue, and peek are O(1)."""
    def __init__(self)->None:
        self._front:Optional[_Node[T]]=None; self._rear:Optional[_Node[T]]=None; self._size=0
    def __len__(self)->int:return self._size
    def __iter__(self)->Iterator[T]:
        node=self._front
        while node is not None:yield node.value; node=node.next
    def is_empty(self)->bool:return self._size==0
    def enqueue(self,value:T)->None:
        """Add value at rear in O(1)."""
        node=_Node(value)
        if self._rear is None:self._front=node
        else:self._rear.next=node
        self._rear=node; self._size+=1
    def dequeue(self)->T:
        """Remove and return front value; raise IndexError when empty."""
        if self._front is None:raise IndexError("dequeue from empty queue")
        value=self._front.value; self._front=self._front.next
        if self._front is None:self._rear=None
        self._size-=1; return value
    def peek(self)->T:
        """Return front value without removing it; raise IndexError when empty."""
        if self._front is None:raise IndexError("peek at empty queue")
        return self._front.value
