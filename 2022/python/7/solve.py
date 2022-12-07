#!/usr/bin/env python3

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def make_system(data):
    current_dir_id = -1
    in_ls = False
    lscounter = 0
    system = [['/']]
    current_dir = system[0]
    curret_dirname = '/'
    PATH = []
    for i in data:
        line = i.replace('\n', '')
        in_command = False

        # UPDATE CURRENT DIR
        current_dir = system
        for direc in range(len(PATH)): #Lê todos os elementos do path
            for i in current_dir:
                if i[0] == PATH[direc]:
                    current_dir = i

        if "$" in line: in_command = True;

            # IN COMMAND BEGIN

        if in_command == True:
            in_ls = False
            command = line
            #print("Entered command state")

            if "$ cd" in command:
                #print("entered CD state")
                dir = command.split(' ')[2]
                if 'cd ..' not in command:
                    current_dir_id += 1; PATH.append(dir)
                    #print(PATH)
                elif 'cd ..' in command:
                    current_dir_id -= 1; PATH.pop()
                    #print(PATH)

            if "$ ls" in command:
                in_ls = True
                lscounter += 1
                #print(f"Entered ls state for the {lscounter}st time")

            # IN COMMAND END

            # IN LS BEGIN

        if in_ls == True:
            line = line.split(' ')
            if line[0] == 'dir':
                dir = line[1]
                if [dir] not in current_dir : current_dir.append([dir])
            if line[0].isnumeric():
                file = (int(line[0]), line[1])
                if file not in current_dir : current_dir.append(file)

    return system

def get_dir_size(dir):
    size = 0
    for item in dir:
        if type(item) == list:
            size += get_dir_size(item)
        if type(item) == tuple:
            size += item[0]
    return size

def return_sep_folders(system):
    folders = []
    for folder in system:
        if type(folder) == list:
            folders.append(folder)
            for i in return_sep_folders(folder):
                folders.append(i)
    return folders

def get_folders_size(folders):
    sizes = []
    for folder in folders:
        sizes.append((folder[0], get_dir_size(folder)))
    return sizes

def solve_first_problem(sizes):
    sum = 0
    for i in sizes:
        if i[1] > 100000:
            pass
        else:
            sum += i[1]
    return sum

def solve_second_problem(sizes):
    total_space = 70000000
    update_size = 30000000
    current_used_space = sizes[0][1]
    current_free_space = total_space - current_used_space
    needed_space = update_size - current_free_space
    valid_folders = []
    valid_sizes = []
    for i in sizes:
        space = i[1]
        if space >= needed_space:
            valid_folders.append(i)
            valid_sizes.append(space)
    return min(valid_sizes)

data = read_file("input.txt")
system = make_system(data)
size = get_dir_size(system)
folders = return_sep_folders(system)
sizes = get_folders_size(folders)
first_answer = solve_first_problem(sizes)
print(f"The first answer is {first_answer}")
print(solve_second_problem(sizes))
