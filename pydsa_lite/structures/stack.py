"""A last-in, first-out stack."""
from __future__ import annotations
from typing import Generic,Iterator,Optional,TypeVar
T=TypeVar("T")
class _Node(Generic[T]):
    def __init__(self,value:T)->None:self.value=value; self.next:Optional[_Node[T]]=None
class Stack(Generic[T]):
    """Linked-node LIFO stack; push, pop, and peek are O(1)."""
    def __init__(self)->None:self._top:Optional[_Node[T]]=None; self._size=0
    def __len__(self)->int:return self._size
    def __iter__(self)->Iterator[T]:
        node=self._top
        while node is not None:yield node.value; node=node.next
    def is_empty(self)->bool:return self._size==0
    def push(self,value:T)->None:
        """Place value on top in O(1)."""
        node=_Node(value); node.next=self._top; self._top=node; self._size+=1
    def pop(self)->T:
        """Remove and return top value; raise IndexError when empty."""
        if self._top is None:raise IndexError("pop from empty stack")
        value=self._top.value; self._top=self._top.next; self._size-=1
        return value
    def peek(self)->T:
        """Return top value without removing it; raise IndexError when empty."""
        if self._top is None:raise IndexError("peek at empty stack")
        return self._top.value
