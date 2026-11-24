import pytest
from pydsa_lite.structures import DoublyLinkedList,SinglyLinkedList

@pytest.mark.parametrize("kind",[SinglyLinkedList,DoublyLinkedList])
def test_basic_operations(kind):
    items=kind()
    assert items.is_empty() and len(items)==0
    items.append(2); items.prepend(1); items.append(3)
    assert list(items)==[1,2,3] and len(items)==3
    assert items.find(2) and not items.find(9)
    items.remove(2); assert list(items)==[1,3]
    with pytest.raises(ValueError):items.remove(99)

def test_singly_pop_front():
    items=SinglyLinkedList([4,5])
    assert items.pop_front()==4 and items.pop_front()==5
    with pytest.raises(IndexError):items.pop_front()

def test_doubly_ends_reverse_and_empty():
    items=DoublyLinkedList([1,2,3])
    assert list(reversed(items))==[3,2,1]
    assert items.pop_front()==1 and items.pop_back()==3 and items.pop_back()==2
    assert items.is_empty() and items._head is None and items._tail is None
    with pytest.raises(IndexError):items.pop_back()

def test_doubly_links_after_middle_removal():
    items=DoublyLinkedList([1,2,3]); items.remove(2)
    assert list(items)==[1,3]
    assert items._head.next.previous is items._head
    assert items._tail.previous.next is items._tail
