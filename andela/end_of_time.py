def reachTheEnd(grid: list, maxTime):

    n = len(grid)

    # start from the end
    grid.reverse()

    gs = []
    for i in range(n):
        cell = grid[i]
        g = []
        for k in range(len(cell)):
            if cell[k] == ".":
                g.append(k)

        gs.append(g)

    print(gs)

    # if a move is possible they should share a index
    common = set(gs[0]).intersection(*gs)
    if len(common) > 0:
        # move is possible
        # we need to calculate the number of moves too

        # if n < maxTime:  # not so correct
        return "Yes"

    return "No"


if __name__ == "__main__":
    print(reachTheEnd(["..##", "#.##", "#..."], 5))
    print(reachTheEnd(["...", "..."], 3))
    print(reachTheEnd([".#", "#."], 3))
