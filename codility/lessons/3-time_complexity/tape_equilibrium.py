from typing import List
from itertools import accumulate
from loguru import logger


def solution(A: List):

    items_length = len(A)
    if items_length == 2:
        return abs(A[0] - A[1])

    ab = []
    for i in range(1, items_length):
        left = A[:i]
        right = A[i:]

        abs_diff = abs(sum(left) - sum(right))
        ab.append(abs_diff)

    # print(ab)
    return min(ab)


def solution2(A: List):
    s = sum(A)
    l = list(accumulate(A[:-1]))
    print(s)
    print(l)

    abs_diff = [abs(2 * x - s) for x in l]
    print(abs_diff)

    return min(abs_diff)


if __name__ == "__main__":
    # print(solution([3, 1, 2, 4, 3]))
    print(solution2([3, 1, 2, 4, 3]))
    # print(solution([3, 1]))
