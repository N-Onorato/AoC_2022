

farm = []
score_farm = []

def main():
    with open("day_08/input.txt") as input_file:
        for line in input_file.readlines():
            line = line.strip()
            farm.append(line)

    for row_n, row in enumerate(farm):
        score_farm.append([scoreTree(row_n, col_n, int(size)) for col_n, size in enumerate(row)])

    print(*score_farm, sep='\n')
    print(sorted([sorted(line, reverse=True)[0] for line in score_farm])[-1])

def scoreTree(row: int, col: int, size: int) -> bool:
        pos = (col, row)
        return (checkUp(pos, size) * checkDown(pos, size) * checkLeft(pos, size) * checkRight(pos, size))


def checkUp(pos, size):
    score = 0
    x, y = pos
    y -= 1
    if y < 0:
        return 0
    while y >= 0: # While on the board
        if size > int(farm[y][x]):
            score += 1
            y -= 1
        else:
            score += 1
            return score
    return score

def checkLeft(pos, size):
    score = 0
    x, y = pos
    x -= 1
    if x < 0:
        return 0
    while x >= 0:
        if size > int(farm[y][x]):
            score += 1
            x -= 1
        else:
            score += 1
            return score
    return score

def checkRight(pos, size):
    score = 0
    x, y = pos
    x += 1
    if x >= len(farm[0]):
        return 0
    while x <= len(farm[0]) - 1:
        if size > int(farm[y][x]):
            score += 1
            x += 1
        else:
            score += 1
            return score
    return score

def checkDown(pos, size):
    score = 0
    x, y = pos
    y += 1
    if y >= len(farm):
        return 0
    while y <= len(farm) - 1:
        if size > int(farm[y][x]):
            score += 1
            y += 1
        else:
            score += 1
            return score
    return score

if __name__ == "__main__":
    main()