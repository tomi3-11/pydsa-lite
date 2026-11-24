"""Singly and doubly linked lists for learning node-based structures."""
from __future__ import annotations
from typing import Generic, Iterator, Optional, TypeVar
T=TypeVar("T")

class _SNode(Generic[T]):
    def __init__(self,value:T)->None:
        self.value=value
        self.next:Optional[_SNode[T]]=None

class SinglyLinkedList(Generic[T]):
    """Forward-only node chain. Prepend/pop_front O(1); append/search/remove O(n)."""
    def __init__(self,values=None)->None:
        self._head:Optional[_SNode[T]]=None
        self._size=0
        if values is not None:
            for value in values:self.append(value)
    def __len__(self)->int:return self._size
    def __iter__(self)->Iterator[T]:
        node=self._head
        while node is not None:
            yield node.value
            node=node.next
    def __repr__(self)->str:return f"SinglyLinkedList({list(self)!r})"
    def is_empty(self)->bool:return self._size==0
    def prepend(self,value:T)->None:
        """Insert at head in O(1)."""
        node=_SNode(value); node.next=self._head; self._head=node; self._size+=1
    def append(self,value:T)->None:
        """Insert at tail in O(n), since only the head is stored."""
        node=_SNode(value)
        if self._head is None:self._head=node
        else:
            current=self._head
            while current.next is not None:current=current.next
            current.next=node
        self._size+=1
    def find(self,value:T)->bool:
        """Return whether value occurs; O(n)."""
        return any(item==value for item in self)
    def remove(self,value:T)->None:
        """Remove first matching value or raise ValueError."""
        previous=None; current=self._head
        while current is not None:
            if current.value==value:
                if previous is None:self._head=current.next
                else:previous.next=current.next
                self._size-=1; return
            previous,current=current,current.next
        raise ValueError(f"{value!r} is not in the list")
    def pop_front(self)->T:
        """Remove and return head in O(1); empty list raises IndexError."""
        if self._head is None:raise IndexError("pop from empty linked list")
        value=self._head.value; self._head=self._head.next; self._size-=1
        return value

class _DNode(Generic[T]):
    def __init__(self,value:T)->None:
        self.value=value
        self.previous:Optional[_DNode[T]]=None
        self.next:Optional[_DNode[T]]=None

class DoublyLinkedList(Generic[T]):
    """Two-way node chain. Both ends are tracked for O(1) end operations."""
    def __init__(self,values=None)->None:
        self._head:Optional[_DNode[T]]=None; self._tail:Optional[_DNode[T]]=None; self._size=0
        if values is not None:
            for value in values:self.append(value)
    def __len__(self)->int:return self._size
    def __iter__(self)->Iterator[T]:
        node=self._head
        while node is not None:
            yield node.value; node=node.next
    def __reversed__(self)->Iterator[T]:
        node=self._tail
        while node is not None:
            yield node.value; node=node.previous
    def __repr__(self)->str:return f"DoublyLinkedList({list(self)!r})"
    def is_empty(self)->bool:return self._size==0
    def prepend(self,value:T)->None:
        """Insert at head in O(1)."""
        node=_DNode(value); node.next=self._head
        if self._head is None:self._tail=node
        else:self._head.previous=node
        self._head=node; self._size+=1
    def append(self,value:T)->None:
        """Insert at tail in O(1)."""
        node=_DNode(value); node.previous=self._tail
        if self._tail is None:self._head=node
        else:self._tail.next=node
        self._tail=node; self._size+=1
    def find(self,value:T)->bool:
        """Return whether value occurs; O(n)."""
        return any(item==value for item in self)
    def remove(self,value:T)->None:
        """Remove first matching value, reconnecting both neighboring links."""
        node=self._head
        while node is not None:
            if node.value==value:
                if node.previous is None:self._head=node.next
                else:node.previous.next=node.next
                if node.next is None:self._tail=node.previous
                else:node.next.previous=node.previous
                self._size-=1; return
            node=node.next
        raise ValueError(f"{value!r} is not in the list")
    def pop_front(self)->T:
        """Remove head in O(1); empty list raises IndexError."""
        if self._head is None:raise IndexError("pop from empty linked list")
        value=self._head.value; self._head=self._head.next
        if self._head is None:self._tail=None
        else:self._head.previous=None
        self._size-=1; return value
    def pop_back(self)->T:
        """Remove tail in O(1); empty list raises IndexError."""
        if self._tail is None:raise IndexError("pop from empty linked list")
        value=self._tail.value; self._tail=self._tail.previous
        if self._tail is None:self._head=None
        else:self._tail.next=None
        self._size-=1; return value
