import pytest
from pydsa_lite.structures import BinarySearchTree

def test_insert_search_and_sorted_iteration():
    tree = BinarySearchTree[int]()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        assert tree.insert(value)
    assert not tree.insert(6)
    assert len(tree) == 9
    assert 7 in tree
    assert 99 not in tree
    assert tree.find(4) == 4
    assert list(tree) == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_remove_leaf_one_child_and_two_children():
    tree = BinarySearchTree[int]()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]: tree.insert(value)
    tree.remove(1)
    tree.remove(14)
    tree.remove(3)
    assert list(tree) == [4, 6, 7, 8, 10, 13]
    assert len(tree) == 6

def test_remove_root_and_missing_values():
    tree = BinarySearchTree[int]()
    for value in [2, 1, 3]: tree.insert(value)
    tree.remove(2)
    assert list(tree) == [1, 3]
    with pytest.raises(KeyError): tree.remove(99)
    with pytest.raises(KeyError): tree.find(99)
