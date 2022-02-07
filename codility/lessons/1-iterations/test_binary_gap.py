import pytest
from binary_gap import solution


@pytest.mark.parametrize("value, expected", [(9, 2), (529, 4), (15, 0), (32, 0)])
def test_gaps(value, expected):
    assert solution(value) == expected
