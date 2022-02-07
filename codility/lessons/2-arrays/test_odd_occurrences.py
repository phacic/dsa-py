import pytest
from .odd_occurrences import solution


@pytest.mark.parametrize("values, expected", [([9, 3, 9, 3, 7, 9], 7), ([9], 9)])
def test_solution(values, expected):
    assert solution(values) == expected
