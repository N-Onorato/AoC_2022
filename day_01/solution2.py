

def main():
    with open("day_01/input.txt", 'r') as input_file:
        input_string = input_file.read()
        elf_list = input_string.split('\n\n')
        elf_calories = sorted((convert_elf_to_sum(elf) for elf in elf_list))
        print(f"The top 3 calorie rich elfs have {sum(elf_calories[-3:])} calories.")

def convert_elf_to_sum(elf: str) -> int:
    food_items = [int(item) for item in elf.split('\n')]
    return sum(food_items)


if __name__ == "__main__":
    main()
