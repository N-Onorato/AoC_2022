
def main():
    with open("day_06/input.txt") as input_file:
        contents = input_file.read()
    for n in range(len(contents)):
        if len(set(contents[n:n+14])) == 14:
            print(n+14)
            break

if __name__ == "__main__":
    main()