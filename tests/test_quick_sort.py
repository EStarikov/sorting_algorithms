import pytest
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from sorting_algorithms_package.quick_sort import quick_sort

@pytest.mark.parametrize(
    ["n", "expected"], [([], []), ([2], [2]), ([1, 4, 8], [1, 4, 8]), ([
        8, 1, 5], [1, 5, 8]), ([9, 7, 5, 3], [3, 5, 7, 9]), ([1, 2], [1, 2]), ([2, 1], [1, 2])]
)
def test_sort(n, expected):
    assert quick_sort(n) == expected