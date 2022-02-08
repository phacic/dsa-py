import pytest
from .cyclic_rotate import solution, solution2


@pytest.mark.parametrize(
    "A, K, expected",
    (([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]), ([1, 2, 3, 4], 4, [1, 2, 3, 4])),
)
def test_solution(A, K, expected):
    assert solution(A=A, K=K) == expected


@pytest.mark.parametrize(
    "A, K, expected",
    (([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]), ([1, 2, 3, 4], 4, [1, 2, 3, 4])),
)
def test_solution(A, K, expected):
    assert solution2(A=A, K=K) == expected
