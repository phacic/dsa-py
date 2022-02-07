def solution(A):
    items_length = len(A)
    if items_length == 0:
        return 1

    expected = {x for x in range(1, items_length + 1)}
    diff = list(expected.difference(A))

    if len(diff) > 0:
        return diff[0]

    # if all spaces are filled then the missing number is the
    # next highest number
    mx = max(A)
    return mx + 1


if __name__ == "__main__":
    print(solution([2, 3, 1, 5]))
    print(solution([2, 3, 1, 4]))
    print(solution([]))
    print(solution([2]))
