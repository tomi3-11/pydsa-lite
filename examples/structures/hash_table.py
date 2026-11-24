"""Demonstrate insertion, lookup, replacement, and deletion."""
from pydsa_lite.structures import HashTable

scores = HashTable[str, int]()
scores["Ada"] = 98
scores["Grace"] = 95
scores["Ada"] = 100
print("Ada:", scores["Ada"])
print("Grace exists:", "Grace" in scores)
del scores["Grace"]
print("Remaining keys:", list(scores))
