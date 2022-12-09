

farm = []
visibility_farm = []

def main():
    with open("day_08/input.txt") as input_file:
        for line in input_file.readlines():
            line = line.strip()
            farm.append(line)

    for row_n, row in enumerate(farm):
        visibility_farm.append([isVisible(row_n, col_n, int(size)) for col_n, size in enumerate(row)])

    # print(*visibility_farm, sep='\n')
    print(sum([sum(line) for line in visibility_farm]))

def isVisible(row: int, col: int, size: int) -> bool:
    if row == 0 or col == 0 or row == len(farm) - 1 or col == len(farm[0]) - 1:
        return True
    else:
        pos = (col, row)
        return checkUp(pos, size) or checkDown(pos, size) or checkLeft(pos, size) or checkRight(pos, size) 


def checkUp(pos, size):
    x, y = pos
    y -= 1
    while y >= 0:
        if size > int(farm[y][x]):
            y -= 1
        else:
            return False
    return True

def checkLeft(pos, size):
    x, y = pos
    x -= 1
    while x >= 0:
        if size > int(farm[y][x]):
            x -= 1
        else:
            return False
    return True

def checkRight(pos, size):
    x, y = pos
    x += 1
    while x <= len(farm[0]) - 1:
        if size > int(farm[y][x]):
            x += 1
        else:
            return False
    return True

def checkDown(pos, size):
    x, y = pos
    y += 1
    while y <= len(farm) - 1:
        if size > int(farm[y][x]):
            y += 1
        else:
            return False
    return True

if __name__ == "__main__":
    main()