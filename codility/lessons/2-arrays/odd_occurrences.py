from loguru import logger


@logger.catch
def solution(A):
    items_length = len(A)

    counts = {}

    for i in range(items_length):
        item = A[i]
        counts[item] = counts.get(item, 0) + 1

    filtered_odd = list(filter(lambda elem: elem[1] == 1, counts.items()))
    return filtered_odd[0][0]


if __name__ == "__main__":
    print(solution([9, 3, 9, 3, 7, 9]))
#     print(solution([9]))
