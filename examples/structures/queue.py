"""Demonstrate first-in, first-out queue behavior.

Run after installing the project in editable mode:
    python examples/structures/queue.py
"""

from pydsa_lite.structures import Queue

print_jobs = Queue[str]()
print_jobs.enqueue("report.pdf")
print_jobs.enqueue("notes.txt")
print_jobs.enqueue("photo.png")

# The first job enqueued is the first job processed.
while not print_jobs.is_empty():
    print("Printing:", print_jobs.dequeue())
