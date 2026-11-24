"""Demonstrate last-in, first-out stack behavior.

Run after installing the project in editable mode:
    python examples/structures/stack.py
"""

from pydsa_lite.structures import Stack

history = Stack[str]()
history.push("open file")
history.push("edit file")
history.push("save file")

# The last action pushed is the first action removed.
while not history.is_empty():
    print("Undo:", history.pop())
