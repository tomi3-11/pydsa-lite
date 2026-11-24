import pytest
from pydsa_lite.structures import Queue

def test_fifo_and_iteration():
    queue=Queue(); queue.enqueue("first"); queue.enqueue("second")
    assert len(queue)==2 and queue.peek()=="first"
    assert list(queue)==["first","second"]
    assert queue.dequeue()=="first" and queue.dequeue()=="second" and queue.is_empty()

def test_reuse_after_empty():
    queue=Queue(); queue.enqueue(1); assert queue.dequeue()==1
    queue.enqueue(2); assert queue.dequeue()==2
    assert queue._front is None and queue._rear is None

def test_empty_operations_raise():
    queue=Queue()
    with pytest.raises(IndexError):queue.dequeue()
    with pytest.raises(IndexError):queue.peek()
