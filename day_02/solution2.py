from typing import Tuple, List

def main():
    with open("day_02/input.txt") as input_file:
        pairs = parse_input(input_file.read())
    scores = [calc_score(pair) for pair in pairs]
    print(f"Sum of scores is {sum(scores)}")

def calc_score(pair: Tuple[str, str]) -> int:
    match pair:
        case ('A', "X"):
            return 3
        case ('A', "Y"):
            return 4
        case ('A', "Z"):
            return 8
        case ('B', "X"):
            return 1
        case ('B', "Y"):
            return 5
        case ('B', 'Z'):
            return 9
        case ('C', 'X'):
            return 2
        case ('C', 'Y'):
            return 6
        case ('C', 'Z'):
            return 7

def parse_input(input: str) ->List[Tuple[str, str]]:
    return [tuple(pair.split(' ')) for pair in input.split('\n')]

if __name__ == "__main__":
    main()