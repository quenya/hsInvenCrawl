def read_last_num():
    with open('last.txt') as last_file:
        return int(last_file.readline())


def write_last_num(last_num):
    with open('last.txt', 'w') as last_file:
        last_file.write(str(last_num))