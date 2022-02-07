from loguru import logger
from math import ceil


def solution(X, Y, D):

    j = (Y - X) / D

    return ceil(j)


if __name__ == "__main__":
    print(solution(10, 85, 30))
