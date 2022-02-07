import pytest
from .tape_equilibrium import solution


@pytest.mark.parametrize("points, least", [((3, 1, 2, 4, 3), 1)])
def test_solution(points, least):
    assert solution(points) == least
