def read_file(filename):

    with open(filename, 'r') as f:
        data_r = f.readlines()
    data = []
    for i in data_r:
        i = i.replace("\n", "")
        appnd = []
        for x in i:
            appnd.append(int(x))
        data.append(appnd)
    return data

def return_column_list(data, cords):
    column_list = []
    column_index = cords[1]
    for row in range(len(data)):
        row_list = data[row]
        for c in range(len(row_list)):
            c_item = row_list[c]
            if c == column_index:
                column_list.append(c_item)

    return column_list


def remove_right_bottom(vector, cords):
    column = cords[1]
    lv = len(vector)
    new_vector = [i for i in vector]
    while lv != column:
        new_vector.pop()
        lv -= 1
    new_vector.reverse()
    return new_vector

def check_axis(vector, element_cords):
    counter_dl = 0
    counter_ur = 0
    column = element_cords[1]
    element = vector[column]
    for i in range(len(vector)):
        e = vector[i]
        if i < column:
            if e >= element:
                counter_dl += 1
        if i > column:
            if e >= element:
                counter_ur += 1
    return (counter_dl, counter_ur)

def remove_left_up(vector, cords):
    column = cords[1]
    lv = len(vector)
    new_vector = [i for i in vector]
    for i in range(lv):
        if i == column:
            break
        new_vector.pop(0)
    new_vector.pop(0)
    return new_vector

def check_sight(vec, vec_c, cords, cords_y):
    element = vec[cords[1]]
    l = remove_right_bottom(vec, cords)
    r = remove_left_up(vec, cords)
    u = remove_right_bottom(vec_c, cords_y)
    d = remove_left_up(vec_c, cords_y)

    counter_vl = 0
    counter_vr = 0
    counter_vd = 0
    counter_vu = 0
    for i in l:
        counter_vl += 1
        if i >= element:
            break
    for i in r:
        counter_vr += 1
        if i >= element:
            break
    for i in u:
        counter_vu += 1
        if i >= element:
            break
    for i in d:
        counter_vd += 1
        if i >= element:
            break
    return (counter_vl, counter_vr, counter_vu, counter_vd)

def solve_1(data):
    vis = 0
    scenic = 0
    total = 0
    for row_index in range(len(data)):
        row = data[row_index]
        for column_index in range(len(row)):
            element = row[column_index]
            cords_x = (row_index, column_index)
            cords_y = (column_index, row_index)
            x_axis = row
            y_axis = return_column_list(data, cords_x)
            VL, VR = check_axis(x_axis, cords_x)
            VU, VD = check_axis(y_axis, cords_y)

            SL, SR, SU, SD = check_sight(x_axis, y_axis, cords_x, cords_y)
            scenic_new = SL * SR * SU * SD
            if scenic_new > scenic:
                scenic = scenic_new


            total += 1
            if VL == 0 or VR == 0 or VU == 0 or VD == 0:
                vis += 1
    return vis, scenic

data = read_file("input.txt")
for i in data:
    print(i)
print('\n'*2)

print(data[1])
print(solve_1(data))
