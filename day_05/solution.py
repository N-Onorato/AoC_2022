from typing import List
from collections import deque
from itertools import repeat
from more_itertools import collapse
import re

initial = [
    deque([]),
    deque("BGSC"),
    deque("TMWHJNVG"),
    deque("MQS"),
    deque("BSLTWNM"),
    deque("JZFTVGWP"),
    deque("CTBGQHS"),
    deque("TJPBW"),
    deque("GDCZFTQM"),
    deque("NSHBPF")
]

def main():
    with open("day_05/input.txt") as input_file:
        file_content = input_file.read()
    instructions = re.finditer("^move (\d{1,2}) from (\d{1,2}) to (\d{1,2})", file_content, flags=re.MULTILINE)
    steps = (map(int, n.groups()) for n in instructions)
    moves = collapse((repeat((s, d), n) for n, s, d in steps), base_type=tuple)
    [move(s, d, initial) for s, d, in moves]
    print(*initial, sep='\n')

def move(source: int, destination: int, stacks: List[deque]):
    stacks[destination].append(stacks[source].pop())




if __name__ == "__main__":
    main()


