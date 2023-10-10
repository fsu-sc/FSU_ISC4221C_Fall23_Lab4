import pytest
from answers_lab import read_graph

# Test read_graph() function
def test_read_graph():
    # Test reading a valid graph file
    edge_list, n_edges, n_nodes, degrees = read_graph('walther_edges.txt')
    assert len(edge_list) == 31 
    assert n_edges == 31
    assert n_nodes == 25
    x = [3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 2, 1, 3, 3, 3, 2, 2, 3, 2, 3, 1, 2, 3, 3, 1]
	# assert all(x[i] == degrees[i] for i in range(n_nodes))