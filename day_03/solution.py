
prioritization = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    with open("day_03/input.txt") as file_input:
        rucksacks = parse_input(file_input.read())
        duplicates = [sack[0].intersection(sack[1]) for sack in rucksacks]
        print(sum([prioritization.index(dupe.pop()) for dupe in duplicates]))
    pass

def parse_input(input_str):
    return [(set(sack[:int(len(sack)/2)]), set(sack[int(len(sack)/2):])) for sack in input_str.split('\n')]

if __name__ == "__main__":
    main()