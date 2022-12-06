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
    [move(n, s, d, initial) for n, s, d, in steps]
    print(*initial, sep="\n")

def move(size: int, source: int, destination: int, stacks: List[deque]):
    temp_queue = deque()
    for n in range(size):
        temp_queue.append(stacks[source].pop())
    for n in range(size):
        stacks[destination].append(temp_queue.pop())





if __name__ == "__main__":
    main()


