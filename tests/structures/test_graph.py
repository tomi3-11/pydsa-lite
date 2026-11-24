import pytest
from pydsa_lite.structures import Graph

def test_undirected_edges_and_implicit_vertices():
    graph = Graph[str]()
    graph.add_edge("A", "B", 2.5)
    assert len(graph) == 2
    assert graph.has_edge("A", "B")
    assert graph.has_edge("B", "A")
    assert graph.neighbors("A") == ("B",)
    assert graph.edge_weight("B", "A") == 2.5
    assert graph.degree("A") == 1

def test_directed_edges_and_duplicate_edge_update():
    graph = Graph[str](directed=True)
    graph.add_edge("A", "B")
    graph.add_edge("A", "B", 4)
    assert graph.has_edge("A", "B")
    assert not graph.has_edge("B", "A")
    assert graph.edge_weight("A", "B") == 4
    assert len(graph) == 2

def test_remove_edges_and_vertices():
    graph = Graph[int]()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.remove_edge(1, 2)
    assert not graph.has_edge(1, 2)
    assert not graph.has_edge(2, 1)
    graph.remove_vertex(2)
    assert list(graph) == [1, 3]
    assert graph.neighbors(1) == ()

def test_missing_vertex_and_edge_raise():
    graph = Graph[int]()
    with pytest.raises(KeyError): graph.neighbors(10)
    with pytest.raises(KeyError): graph.remove_vertex(10)
    with pytest.raises(KeyError): graph.remove_edge(1, 2)
    with pytest.raises(KeyError): graph.edge_weight(1, 2)
