def solution(n: int) -> int:

    b = to_bin(n)

    if len(b) < 3:
        return 0

    gaps = []
    gap_count = 0
    for i in range(len(b)):
        if b[i] == "1":
            # gap stop. save gap and start counting again
            gaps.append(gap_count)
            # reset gap count
            gap_count = 0
        else:
            # gap found
            gap_count += 1

    print(gaps)
    return max(gaps)


def solution2(n: int) -> int:
    b = to_bin(n)
    len_b = len(b)
    if len_b < 3:
        return 0

    max_gap = 0
    gap_counter = 0
    for i in range(len_b):
        if b[i] == "1":
            max_gap = gap_counter if gap_counter > max_gap else max_gap
            # reset counter
            gap_counter = 0
        else:
            gap_counter += 1

    return max_gap


def to_bin(n: int) -> str:
    """convert number to binary """
    b = bin(n)
    return b[2:]


if __name__ == "__main__":
    print(solution(1041))
    print(solution2(1041))

    print(solution(32))
    print(solution2(32))
