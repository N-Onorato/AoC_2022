from dataclasses import dataclass, field
from typing import Generator
from more_itertools import chunked

@dataclass
class SimpleMachine:
    x: int
    cycle: int
    program: Generator

    def process(self):
        for command in self.program:
            match command.strip().split(' '):
                case ["noop"]:
                    self.cycle += 1
                    yield self.snapshot()
                case ["addx", n]:
                    self.cycle += 1
                    yield self.snapshot()
                    self.cycle += 1
                    yield self.snapshot()
                    self.x += int(n)

    def snapshot(self) -> tuple:
        return (self.cycle, self.x)



def main():
    with open("day_10/input.txt") as input_file:
        program = (command for command in input_file.readlines())
        computer = SimpleMachine(1, 0, program)
        screen = list("." * 40 * 6)
        for state in computer.process():
            col = state[0] % 40 - 1
            if(col in (state[1] -1, state[1], state[1] + 1)):
                screen[state[0] - 1] = '#'
        print(*["".join(chunk) for chunk in chunked(screen, 40)], sep='\n')


if __name__ == "__main__":
    main()

