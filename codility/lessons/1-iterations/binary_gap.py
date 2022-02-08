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


def to_bin(n: int) -> str:
    """convert number to binary """
    b = bin(n)
    return b[2:]


if __name__ == "__main__":
    print(solution(1041))
#     print(solution(32))
