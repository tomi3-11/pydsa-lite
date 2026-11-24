"""Demonstrate ordered insertion, lookup, traversal, and removal."""
from pydsa_lite.structures import BinarySearchTree

numbers = BinarySearchTree[int]()
for number in [8, 3, 10, 1, 6, 14, 4, 7, 13]: numbers.insert(number)
print("Sorted values:", list(numbers))
numbers.remove(3)
print("After removing 3:", list(numbers))
