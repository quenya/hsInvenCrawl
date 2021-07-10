def read_last_num():
    with open('/Users/LeeJongHyun/PycharmProjects/hsInvenCrawl/last.txt') as last_file:
        return int(last_file.readline())


def write_last_num(last_num):
    with open('/Users/LeeJongHyun/PycharmProjects/hsInvenCrawl/last.txt', 'w') as last_file:
        last_file.write(str(last_num))