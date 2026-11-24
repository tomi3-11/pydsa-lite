import pytest

from pydsa_lite.structures import Stack


def test_stack_uses_last_in_first_out_order():
    stack = Stack()
    stack.push("first")
    stack.push("second")

    assert len(stack) == 2
    assert stack.peek() == "second"
    assert list(stack) == ["second", "first"]
    assert stack.pop() == "second"
    assert stack.pop() == "first"
    assert stack.is_empty()


def test_empty_stack_operations_raise_index_error():
    stack = Stack()

    with pytest.raises(IndexError):
        stack.pop()

    with pytest.raises(IndexError):
        stack.peek()
