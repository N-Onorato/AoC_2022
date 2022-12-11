from collections import deque
from typing import Callable, Tuple, List

class Monkey:


    def __init__(self, starting_items: list[int], operation: Callable[[int], int], test: Tuple[int, int, int]):
        self.items = deque(starting_items)
        self.operation = operation
        self.divisor, self.true_monkey, self.false_monkey = test
        self.item_count = 0

    def throw(self, troop: List):
        item = self.items.popleft()
        target = troop[self.true_monkey] if item % self.divisor == 0 else troop[self.false_monkey]
        target.catch(item)

    def catch(self, item: int):
        self.items.append(item)

    def inspect(self):
        self.items[0] = int(self.operation(self.items[0])) % 9_699_690

    def processTurn(self, troop: List):
        if len(troop) > 0:
            for n in range(len(self.items)):
                self.item_count += 1
                self.inspect()
                self.throw(troop)

test_data = [
    Monkey([79, 98],
            lambda old: old * 19,
            (23, 2, 3)),
    Monkey([54, 65, 75, 74],
            lambda old: old + 6,
            (19, 2, 0)),
    Monkey([79, 60, 97],
            lambda old: old**2,
            (13, 1, 3)),
    Monkey([74],
            lambda old: old + 3,
            (17, 0, 1))
]

input_state = [
    Monkey([98, 70, 75, 80, 84, 89, 55, 98],
            lambda old: old * 2,
            (11, 1, 4)),
    Monkey([59],
            lambda old: old**2,
            (19, 7, 3)),
    Monkey([77, 95, 54, 65, 89],
            lambda old: old + 6,
            (7, 0, 5)),
    Monkey([71, 64, 75],
            lambda old: old + 2,
            (17, 6, 2)),
    Monkey([74, 55, 87, 98],
            lambda old: old * 11,
            (3, 1, 7)),
    Monkey([90, 98, 85, 52, 91, 60],
            lambda old: old + 7,
            (5, 0, 4)),
    Monkey([99, 51],
            lambda old: old + 1,
            (13, 5, 2)),
    Monkey([98, 94, 59, 76, 51, 65, 75],
            lambda old: old + 5,
            (2, 3, 6))
]