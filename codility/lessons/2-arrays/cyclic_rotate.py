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


def solution2(A: List, K: int):
    """
    rotate A, K times

    if value of K is within the length of the Array (K <= length(A)) then, 
    the item at the Kth will be the first item at the end of the rotation.

    The issue with this approach is that of when K > length(A) then we could
    use K mod length(A) to find the new K
    """

    # find the start index 
    start_index = K - 1

    head = A[start_index:]
    tail = A[:start_index]

    return head + tail


if __name__ == "__main__":
    # print(solution([3, 8, 9, 7, 6], 3))
    print(solution2([3, 8, 9, 7, 6], 3))

#     print(solution([0, 0, 0], 1))
#     print(solution([1, 2, 3, 4], 4))
