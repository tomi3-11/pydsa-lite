import pytest

from pydsa_lite.structures import Queue


def test_queue_uses_first_in_first_out_order():
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")

    assert len(queue) == 2
    assert queue.peek() == "first"
    assert list(queue) == ["first", "second"]
    assert queue.dequeue() == "first"
    assert queue.dequeue() == "second"
    assert queue.is_empty()


def test_queue_can_be_reused_after_becoming_empty():
    queue = Queue()
    queue.enqueue(1)

    assert queue.dequeue() == 1

    queue.enqueue(2)
    assert queue.dequeue() == 2
    assert queue._front is None
    assert queue._rear is None


def test_empty_queue_operations_raise_index_error():
    queue = Queue()

    with pytest.raises(IndexError):
        queue.dequeue()

    with pytest.raises(IndexError):
        queue.peek()
