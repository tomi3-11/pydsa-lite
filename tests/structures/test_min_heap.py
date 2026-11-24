import pytest
from pydsa_lite.structures import MinHeap

def test_heapify_and_pop_in_sorted_order():
    heap = MinHeap([7, 2, 9, 1, 5])
    assert heap.peek() == 1
    assert [heap.pop() for _ in range(5)] == [1, 2, 5, 7, 9]
    assert len(heap) == 0

def test_push_duplicates_and_negative_values():
    heap = MinHeap[int]()
    for value in [3, -1, 3, 0]: heap.push(value)
    assert [heap.pop() for _ in range(4)] == [-1, 0, 3, 3]

def test_empty_operations_raise():
    heap = MinHeap()
    with pytest.raises(IndexError): heap.peek()
    with pytest.raises(IndexError): heap.pop()
