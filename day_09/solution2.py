from dataclasses import dataclass

@dataclass
class Vector:
    x: int
    y: int

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def mag(self):
        return self.x**2 + self.y**2

    def __hash__(self):
        return hash((self.x, self.y))

    def normalize(self):
        magnitude = self.mag()
        self.x = int(round(self.x**2 / magnitude))
        self.y = int(round(self.y**2 / magnitude))
        return self

    def asTuple(self) -> tuple:
        return (self.x, self.y)
    
rope = [Vector(0, 0) for n in range(10)]
tail_history = [Vector(0, 0)]

def main():
    with open("day_09/input.txt") as input_file:
        instructions = [line.strip() for line in input_file.readlines()]
        [processInstruction(inst) for inst in instructions]

    #print(*tail_history, sep='\n')
    unique_moves = set(tail_history)
    print(f"The tail moved to {len(unique_moves)} unique spots.")


def processInstruction(code: str):
    direction, steps = code.split(' ')
    steps = int(steps)
    for step in range(steps):
        updateHead(direction)
        for segment in range(1, 10):
            updateSegment(segment)

def updateHead(direction: str):
    match direction:
        case 'U':
            rope[0].y += 1
        case 'R':
            rope[0].x += 1
        case 'D':
            rope[0].y -= 1
        case 'L':
            rope[0].x -= 1

def updateSegment(index):
    diff = rope[index - 1] - rope[index]
    if(diff.mag() > 2):
        match diff.asTuple():
            case (0, y):
                rope[index] += Vector(0, int(diff.y / abs(diff.y)))
            case (x, 0):
                rope[index] += Vector(int(diff.x / abs(diff.x)), 0)
            case(x, y) if x > 0 and y > 0:
                rope[index] += Vector(1, 1)
            case(x, y) if x > 0 and y < 0:
                rope[index]+= Vector(1, -1)
            case(x, y) if x < 0 and y > 0:
                rope[index] += Vector(-1, 1)
            case(x, y) if x < 0 and y < 0:
                rope[index] += Vector(-1, -1)
        if(index == 9):
            tail_history.append(rope[index])

    

if __name__ == "__main__":
    main()