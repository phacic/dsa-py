from typing import List


def solution(A: List, K: int):

    items_length = len(A)

    # placeholder new items
    new_items = [0] * items_length
    for i in range(items_length):
        r = rotate(K, i, items_length)
        new_items[r] = A[i]

    return new_items


def rotate(times, index, length):
    """rotate index number of times"""

    return (index + times) % length


# if __name__ == "__main__":
#     print(solution([3, 8, 9, 7, 6], 3))
#     print(solution([0, 0, 0], 1))
#     print(solution([1, 2, 3, 4], 4))
