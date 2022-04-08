from collections import Counter
from loguru import logger
# from notations import notation


@logger.catch
def solution(A):
    items_length = len(A)

    counts = {}

    for i in range(items_length):
        item = A[i]
        counts[item] = counts.get(item, 0) + 1

    filtered_odd = list(filter(lambda elem: elem[1] == 1, counts.items()))
    return filtered_odd[0][0]


# @logger.catch
# def solution2(items: list):
#     len_a = len(items)

#     items.sort()
#     print(items)
#     # for i in range(0, len_a - 1, 2):
#     #     # print(i, A[i])
#     #     if A[i] != A[i + 1]:
#     #         return A[i]

#     # return A[len_a - 1]

#     return next(
#         (items[i] for i in range(0, len_a - 1, 2) if items[i] != items[i + 1]),
#         items[len_a - 1]
#     )


def solution3(A: list):
    len_a = len(A)
    counts = {}
    odd_item = None
    for i in range(len_a):
        value = counts.get(A[i], 0) + 1
        counts[A[i]] = value
        if value == 1:
            odd_item = A[i]

    return odd_item



if __name__ == "__main__":
    v = [9, 3, 9, 3, 7, 9]
    print(solution(v))
    print(solution3(v))

    
#     print(solution([9]))
    v = [1, 2, 3, 3, 2, 1, 4, 4, 5]
    print(solution(v))
    print(solution3(v))

    # print(notation(solution))
    # print(notation(solution3))
