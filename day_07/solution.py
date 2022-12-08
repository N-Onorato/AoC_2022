from dataclasses import dataclass, field
from typing import Any
from collections import deque
from functools import reduce

@dataclass
class File:
    name: str
    size: int

@dataclass
class Dir:
    loc: str
    parent: Any
    contents: dict = field(default_factory=dict)

    def get_size(self):
        n = 0
        for item in self.contents.values():
            if(isinstance(item, Dir)):
                n += item.get_size()
            else:
                n += item.size
        return n
    
    def add_dir(self, new_dir):
        self.contents[new_dir.loc] = new_dir

    def add_file(self, new_file: File):
        self.contents[new_file.name] = new_file

    def cd(self, new_loc : str):
        child = self.contents[new_loc]
        return child
    
    def up(self):
        return self.parent





def main():
    with open("day_07/test_data.txt", 'r') as input_file:
        content = input_file.readlines()
    filesystem = Dir("/", parent=None)
    for line in content:
        match line.strip().split(' '):
            case "$", "cd", "/":
                pass
            case "$", "cd", "..":
                filesystem = filesystem.up()
            case "$", "cd", new_loc:
                filesystem = filesystem.cd(new_loc)
            case size, filename if size.isnumeric():
                filesystem.add_file(File(filename, int(size)))
            case "dir", directory:
                filesystem.add_dir(Dir(directory, filesystem))
            case _:
                pass

    print(filesystem)

if __name__ == "__main__":
    main()