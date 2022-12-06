
def main():
    with open("day_06/input.txt") as input_file:
        contents = input_file.read()
    for n in range(len(contents)):
        if len(set(contents[n:n+4])) == 4:
            print(n+4)
            break

if __name__ == "__main__":
    main()