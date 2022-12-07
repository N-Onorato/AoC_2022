from collections import deque
location = deque()
location.a

def main():
    with open("day_07/input.txt", 'r') as input_file:
        content = input_file.readlines()
    for line in content:
        match line.split(' '):
            case "$", "cd", "/":
                location = deque("/")
            case "$", "cd", new_loc:
                location.append(new_loc)
            case "$", "cd", "..":
                location.pop()
            case int as size, filename:
                pass
            
    pass


if __name__ == "__main__":
    main()