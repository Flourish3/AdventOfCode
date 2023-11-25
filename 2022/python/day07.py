class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

class Directory:
    def __init__(self, files, dirs, name, parent) -> None:
        self.files = files
        self.dirs = dirs
        self.name = name
        self.parent = parent

if __name__ == "__main__":
    with open("2022/data/day07.txt") as f:
        current_directory = None
        current_command = ""
        main_folder = None
        for l in f.readlines():
            commnads = l.strip().split(" ")
            if commnads[0] == "$":
                current_command = commnads[1]
                if current_command == "cd":
                    if current_directory == None:
                        current_directory = Directory([],[], commnads[2], None)
                        main_folder = current_directory
                    elif commnads[2] == "..":
                        current_directory = current_directory.parent
                    else:
                        new_directory = Directory([], [], commnads[2], current_directory)
                        current_directory.dirs.append(new_directory)
                        current_directory = new_directory
                elif current_command == "ls":
                   pass
            else:
                if current_command == "ls":
                    if commnads[0] == "dir":
                        new_directory = Directory([], [], commnads[1], current_directory)
                        current_directory.dirs.append()

        print(main_folder.name)
        print(main_folder.dirs)

    