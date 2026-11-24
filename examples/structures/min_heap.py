"""Demonstrate how a min-heap returns values in priority order."""
from pydsa_lite.structures import MinHeap

tasks = MinHeap([5, 2, 8, 1])
tasks.push(3)
while len(tasks):
    print("Next smallest:", tasks.pop())
