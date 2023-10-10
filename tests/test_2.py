import pytest
from answers_lab import find_path

# Test find_path() function
def test_find_path():
    # Test finding a path that exists
    edges = [(0, 1), (1, 3), (3, 4), (4, 1), (5,2)]
    assert find_path(edges, 1, 3) == True
    assert find_path(edges, 0, 4) == True
    assert find_path(edges, 0, 5) == False