from more_itertools import grouper

prioritization = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    with open("day_03/input.txt") as file_input:
        rucksacks = parse_input(file_input.read())
        identifier = [sack[0].intersection(sack[1]).intersection(sack[2]) for sack in rucksacks]
        print(sum([prioritization.index(dupe.pop()) for dupe in identifier]))
    pass

def parse_input(input_str):

    return [[set(sack) for sack in group] for group in grouper(input_str.split('\n'), 3)]

if __name__ == "__main__":
    main()