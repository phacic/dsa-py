from typing import List


def count(A: List):
    n = len(A)
    counts = [0] * n
    for k in range(n):
        counts[A[k]] += 1

    return counts


def count2(A: List, m):
    n = len(A)
    counts = [0] * (m + 1)
    for k in range(n):
        counts[A[k]] += 1

    return counts


def swap_slow(A, B, m):
    """swap operation to make A and B equal"""

    n = len(A)
    m = len(B)

    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(m):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True

            # return to initial state
            sum_a -= change
            sum_b += change

    return False


if __name__ == "__main__":
    print(count([0, 0, 4, 2, 4, 5]))
    # print(count2([0, 0, 4, 2, 4, 5], 5))
