def numPlayers(k, scores: list):
    scores.sort()
    scores.reverse()

    n = len(scores)
    ranks = []

    for i in range(n):
        # current position
        position = i + 1

        # previous index
        prev = i - 1
        if prev >= 0:
            # compare current and previous
            if scores[prev] == scores[i]:
                # add the previous position
                ranks.append(position - 1)
            else:
                ranks.append(position)
        else:
            ranks.append(position)

    # find cutoff
    cutoff = list(filter(lambda x: x <= k, ranks))

    return len(cutoff)


if __name__ == "__main__":
    # print(numPlayers(4, [100, 50, 50, 25]))
    print(numPlayers(4, [20, 40, 60, 80, 100]))
    print(numPlayers(4, [2, 2, 3, 4, 5]))
