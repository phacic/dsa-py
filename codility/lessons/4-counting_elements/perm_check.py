from typing import List
from notations import notation

from loguru import logger


def solution(A: List) -> int:
    n = len(A)
    set_a = {x for x in range(1, n + 1)}
    if len(list(set_a.difference(A))) > 0:
        return 1

    return 0


def solution2(A: List) -> int:
    n = len(A)
    m = max(A)

    # if max and len are not the same
    # something is missing
    if m != n:
        return 0

    # for a single item if its not one
    # its not permutation so return 0
    if n == 1: 
        if A[0] != 1:
            return 0
        return 1

    
    counter = [0] * (m)
    for i in range(n):
        counter[A[i] - 1] += 1

    if min(counter) == 0:
        return 0

    return 1


def solution3(A: List) -> int:
    """ return 1 if list is permutation else 0"""
    n = max(A)

    temp = {}
    for k in range(n):
        temp[A[k - 1]] = k

    if len(temp) == n:
        return 1

    return 0


if __name__ == "__main__":
    # print(solution([4, 1, 3, 2]))
    # print(solution2([4, 1, 3, 2]))
    # print(solution2([4, 1, 3])) 
    # print(solution2([1]))
    # print(solution2([4]))
    # print(solution2([3, 2]))
    # print(solution2([3, 3]))

    # print(notation(solution))
    # print(notation(solution2))

    print(solution2([4, 1, 3]))
    print(solution3([4, 1, 3]))
