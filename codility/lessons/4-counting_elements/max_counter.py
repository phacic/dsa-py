from notations import notation


def solution(N: int, A: list):
    n = len(A)
    counter = [0] * N

    for i in range(n):
        v = A[i]
        if v == (N + 1):
            # set all to the max
            m = max(counter)
            counter = [m] * N

        else:
            counter[A[i] - 1] += 1

    return counter


if __name__ == "__main__":
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
    print(notation((solution)))
