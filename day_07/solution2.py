2
from dataclasses import dataclass, field

from typing import Any

@dataclass
class File:
    name: str
    size: int

@dataclass
class Dir:
    loc: str
    parent: Any
    contents: dict = field(default_factory=dict, repr=False)

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

    def list_dirs(self):
        return [item for item in self.content.values() if isinstance(item, Dir)]



total_space = 70000000
space_needed = 30000000
dir_list = []

def main():
    with open("day_07/input.txt", 'r') as input_file:
        content = input_file.readlines()
    root = Dir("/", parent=None)
    dir_list.append(root)
    filesystem = root
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
                new_dir = Dir(directory, filesystem)
                dir_list.append(new_dir)
                filesystem.add_dir(new_dir)
            case _:
                pass
    
    available_space = total_space - root.get_size()
    needed_space = space_needed - available_space
    selected = list(filter(lambda dir : dir.get_size() >= needed_space, dir_list))
    print(selected.sort(key=Dir.get_size))
    print(selected[0].loc, selected[0].get_size())


if __name__ == "__main__":
    main()