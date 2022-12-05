import time

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def init_state():
    [s1, s2, s3, s4, s5, s6, s7, s8, s9] = [
        ['F', 'R', 'W'],
        ['P', 'W', 'V', 'D', 'C', 'M', 'H', 'T'],
        ['L', 'N', 'Z', 'M', 'P'],
        ['R', 'H', 'C', 'J'],
        ['B', 'T', 'Q', 'H', 'G', 'P', 'C'],
        ['Z', 'F', 'L', 'W', 'C', 'G'],
        ['C', 'G', 'J', 'Z', 'Q', 'L', 'V', 'W'],
        ['C', 'V', 'T', 'W', 'F', 'R', 'N', 'P'],
        ['V', 'S', 'R', 'G', 'H', 'W', 'J']]
    for i in [s1,s2,s3,s4,s5,s6,s7,s8,s9]:
        i.reverse()
    return [s1, s2, s3, s4, s5, s6, s7, s8, s9]

def test_state():
    [s1, s2, s3] = [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']

    ]
    return [s1, s2, s3]

def print_top_boxes(stacks):
    topblist = []
    for i in stacks:
        if len(i) != 0:
            topblist.append(i[len(i)-1])

    topbString = ""
    for i in topblist:
        topbString += i
    return [topblist, topbString]

def move_box_9000(stacks, wb, ws, wf):
    from_stack = stacks[ws-1]
    to_stack = stacks[wf-1]
    for i in range(wb):
        to_stack.append(from_stack.pop())

    stacks[ws-1] = from_stack
    stacks[wf-1] = to_stack
    return stacks

def move_box_9001(stacks, wb, ws, wf):
    from_stack = stacks[ws-1]
    to_stack = stacks[wf-1]
    boxes = []
    for i in range(wb):
        boxes.append(from_stack.pop())
    boxes.reverse()
    for box in boxes:
        to_stack.append(box)
    stacks[ws-1] = from_stack
    stacks[wf-1] = to_stack
    return stacks

def solve1(data, stacks):
    final_stack = []
    first = True
    for i in data:
        i = i.replace('\n', '').split(' ')
        wb, ws, wf = [int(i[1]), int(i[3]), int(i[5])]
        if first:
            final_stack = move_box_9000(stacks, wb, ws, wf)
            first = False
        else:
            final_stack = move_box_9000(final_stack, wb, ws, wf)

    return final_stack

def solve2(data, stacks):
    final_stack = []
    first = True
    for i in data:
        i = i.replace('\n', '').split(' ')
        wb, ws, wf = [int(i[1]), int(i[3]), int(i[5])]
        if first:
            final_stack = move_box_9001(stacks, wb, ws, wf)
            first = False
        else:
            final_stack = move_box_9001(final_stack, wb, ws, wf)

    return final_stack

def main():
    ans1=print_top_boxes( solve1( read_data("input.txt"), init_state() ) )[1]
    ans2=print_top_boxes( solve2( read_data("input.txt"), init_state() ) )[1]
    print(f"The first answer was {ans1}")
    print(f"The second answer was {ans2}")

if __name__ == "__main__":
    ti = time.time()
    main()
    tf = time.time()
    print(f"The time was {tf-ti}")
