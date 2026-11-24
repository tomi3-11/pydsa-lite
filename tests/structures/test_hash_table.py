import pytest
from pydsa_lite.structures import HashTable

class CollisionKey:
    def __init__(self, value): self.value = value
    def __hash__(self): return 1
    def __eq__(self, other):
        return isinstance(other, CollisionKey) and self.value == other.value

def test_insert_lookup_replace_and_delete():
    table = HashTable[str, int]()
    table["age"] = 20
    table["age"] = 21
    table["score"] = 90
    assert table["age"] == 21
    assert table.get("missing") is None
    assert table.get("missing", -1) == -1
    assert len(table) == 2
    assert "score" in table
    del table["age"]
    assert "age" not in table
    assert len(table) == 1

def test_collisions_keep_distinct_keys():
    table = HashTable[CollisionKey, str]()
    first, second = CollisionKey("first"), CollisionKey("second")
    table[first] = "one"
    table[second] = "two"
    assert table[first] == "one"
    assert table[second] == "two"
    assert len(table) == 2

def test_resize_preserves_entries():
    table = HashTable[int, int](initial_capacity=2)
    for value in range(30): table[value] = value * 10
    assert len(table) == 30
    assert all(table[value] == value * 10 for value in range(30))

def test_missing_key_raises_and_unhashable_key_is_rejected():
    table = HashTable()
    with pytest.raises(KeyError): _ = table["missing"]
    with pytest.raises(KeyError): del table["missing"]
    with pytest.raises(TypeError): table[[]] = "not hashable"
