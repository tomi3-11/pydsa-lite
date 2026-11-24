import pytest
from pydsa_lite.structures import Stack

def test_lifo_and_iteration():
    stack=Stack(); stack.push("first"); stack.push("second")
    assert len(stack)==2 and stack.peek()=="second"
    assert list(stack)==["second","first"]
    assert stack.pop()=="second" and stack.pop()=="first" and stack.is_empty()

def test_empty_operations_raise():
    stack=Stack()
    with pytest.raises(IndexError):stack.pop()
    with pytest.raises(IndexError):stack.peek()
