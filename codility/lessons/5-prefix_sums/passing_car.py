from notations import notation


def solution(A: list):

    # find indexes for 0s and 1s
    indexes0 = []
    indexes1 = []

    n = len(A)
    for k in range(n):
        if A[k] == 0:
            indexes0.append(k)
        else:
            indexes1.append(k)

    print(indexes0, indexes1)
    pair = []

    for i in range(len(indexes0)):
        for k in range(len(indexes1)):
            v0 = indexes0[i]
            v1 = indexes1[k]
            if v0 < v1:
                pair.append((v0, v1))

    print(pair)
    nl = len(pair)
    if nl > 1_000_000_000:
        return -1
    
    return nl


def solution1(A: list):
    """ pair indexes of values 0 with 1s"""
    n = len(A)
    pair = []
    for i in range(n):
        if A[i] == 0:
            # if the value is 0 iterate over again
            # skipping over 0s and pairing indexes
            # of non zeroes and pairing the indexes
            for k in range(n):
                if A[k] != 0 and i < k:
                    pair.append((i, k))

    print(pair)

    nl = len(pair)
    if nl > 1_000_000_000:
        return -1
    
    return nl


def solution2(A):
    going_east = 0
    passing = 0
    for num in A:
        if num == 0:
            going_east += 1
        else:
            passing += going_east
            if passing > 10 ** 9:
                return -1
    
    return passing
    

if __name__ == "__main__":
    print(notation(solution))
    print(notation(solution1))

    print(solution([0, 1, 0, 1, 1]))
    print(solution1([0, 1, 0, 1, 1]))
