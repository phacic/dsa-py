from typing import List
from notations import notation

def prefix_sums(items: List) -> List:
    """ consecutive totals of the first n elements in an array """
    n = len(items)
    p = [0] * (n + 1)
    for k in range(1, n + 1):
        p[k] = p[k - 1] + items[k - 1]

    return p


def suffix_sums(items: List, x:int, y:int) -> int:
    """ totals of the k last values """ 
    p = prefix_sums(items)

    return p[y + 1] - p[x]


if __name__ == '__main__':
    print(notation(prefix_sums))
    print(prefix_sums([1, 2, 3, 4, 5]))
    print(suffix_sums([1, 2, 3, 4, 5], 2, 4))
