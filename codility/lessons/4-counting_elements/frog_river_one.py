from typing import List
from loguru import logger
from notations import notation


def solution(X: int, A: List):
    n = len(A)

    # expected positions to be filled for
    # jump to be posible
    e = {x for x in range(1, X + 1)}

    # positions as the leaves fall
    p = set()

    for i in range(n):
        p.add(A[i])
        if len(e.difference(p)) < 1:
            return i

    return -1


def solution2(X: int, A: list):
    n = len(A)
    i = 0
    temp = {}
    while i < n:
        temp[A[i]] = i
        if len(temp) == X:
            return i
        i += 1

    return -1


def solution3(X: int, A: list):
    n = len(A)
    temp = {}
    for i in range(n):
        temp[A[i]] = i
        if len(temp) == X:
            return i

    return -1


if __name__ == "__main__":
    # print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    # print(solution(2, [2, 2, 2, 2, 2]))
    # print(solution(2, [1, 2, 2, 2, 2]))

    # print(solution2(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    print(solution3(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    # print(notation(solution))
    # print(notation(solution2))
