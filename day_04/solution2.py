from dataclasses import dataclass
from typing import Tuple

@dataclass
class AssignmentRange():
    mininmum: int
    maximum: int
    length: int

def main():
    with open("day_04/input.txt") as input_file:
            assignment_pairs = [parse_input(line) for line in input_file.read().splitlines()]
    print(len(list(filter(hasOverlap, assignment_pairs))), sep='\n')

def hasOverlap(pair: Tuple[AssignmentRange, AssignmentRange]) -> bool:
    second, first = pair if pair[0].length > pair[1].length else (pair[1], pair[0])
    return (first.mininmum >= second.mininmum and first.mininmum <= second.maximum 
         or first.maximum >= second.mininmum and first.maximum <= second.maximum)

def parse_input(input_pair: str) -> Tuple[AssignmentRange, AssignmentRange]:
    return [parse_range(assignment) for assignment in input_pair.split(',')]

def parse_range(input_range: str):
    low, high = [int(n) for n in input_range.split('-')]
    length = high - low + 1
    return AssignmentRange(low, high, length)

if __name__ == "__main__":
    main()