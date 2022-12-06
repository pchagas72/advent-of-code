def read_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data[0].replace('\n', '')

def detect_signal(noisy_packet, tom):
    size = 0
    if tom == "message": size = 14
    if tom == "packet": size = 4
    chars = []
    temp = []
    for i in noisy_packet:
        temp.append(i)
        chars.append(i)
        if len(temp) == size:
            rsum = 0
            for k in temp:
                r = temp.count(k)
                rsum += r
            if rsum != size:
                temp.pop(0)
            elif rsum == size:
                break
    return len(chars)

data_noisy= read_data('input.txt')
first_answer = detect_signal(data_noisy, "packet")
second_answer = detect_signal(data_noisy, "message")
print(f"The first answer was {first_answer}")
print(f"The second answer was {second_answer}")
