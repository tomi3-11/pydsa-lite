import pytest

from pydsa_lite.structures import DoublyLinkedList, SinglyLinkedList


@pytest.mark.parametrize("list_type", [SinglyLinkedList, DoublyLinkedList])
def test_empty_and_basic_operations(list_type):
    items = list_type()

    assert items.is_empty()
    assert len(items) == 0
    assert list(items) == []

    items.append(2)
    items.prepend(1)
    items.append(3)

    assert list(items) == [1, 2, 3]
    assert len(items) == 3
    assert items.find(2)
    assert not items.find(9)

    items.remove(2)
    assert list(items) == [1, 3]


@pytest.mark.parametrize("list_type", [SinglyLinkedList, DoublyLinkedList])
def test_remove_first_and_last_node(list_type):
    items = list_type([10])
    items.remove(10)

    assert items.is_empty()
    assert len(items) == 0
    assert list(items) == []


@pytest.mark.parametrize("list_type", [SinglyLinkedList, DoublyLinkedList])
def test_remove_missing_value_raises(list_type):
    items = list_type([1, 2])

    with pytest.raises(ValueError):
        items.remove(99)


def test_singly_pop_front_and_empty_error():
    items = SinglyLinkedList([4, 5])

    assert items.pop_front() == 4
    assert items.pop_front() == 5

    with pytest.raises(IndexError):
        items.pop_front()


def test_singly_remove_only_first_duplicate():
    items = SinglyLinkedList([7, 7, 8])

    items.remove(7)

    assert list(items) == [7, 8]
    assert len(items) == 2


def test_doubly_pop_both_ends_and_reverse():
    items = DoublyLinkedList([1, 2, 3])

    assert list(reversed(items)) == [3, 2, 1]
    assert items.pop_front() == 1
    assert items.pop_back() == 3
    assert items.pop_back() == 2
    assert items.is_empty()
    assert items._head is None
    assert items._tail is None

    with pytest.raises(IndexError):
        items.pop_back()


def test_doubly_remove_head_and_tail_preserves_end_links():
    items = DoublyLinkedList([1, 2, 3, 4])

    items.remove(1)
    assert list(items) == [2, 3, 4]
    assert items._head.previous is None

    items.remove(4)
    assert list(items) == [2, 3]
    assert items._tail.next is None
    assert list(reversed(items)) == [3, 2]


def test_doubly_links_are_reconnected_after_middle_removal():
    items = DoublyLinkedList([1, 2, 3])
    items.remove(2)

    assert list(items) == [1, 3]
    assert items._head.next.previous is items._head
    assert items._tail.previous.next is items._tail
