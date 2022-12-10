from dataclasses import dataclass, field
from typing import Generator

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
        signal_strengths = [state[0] * state[1] for state in computer.process() if state[0] in (20, 60, 100, 140, 180, 220)]
        print(sum(signal_strengths))


if __name__ == "__main__":
    main()