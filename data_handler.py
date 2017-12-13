import os

dir_path = os.path.dirname(os.path.realpath(__file__))
key_index = 0
value_index = 1


def read_file(filename):
    res_dict = {}
    with open(dir_path + filename, 'r') as f:
        for line in f:
            line_list = line.split(': ')
            res_dict[line_list[key_index]] = line_list[value_index]
    return res_dict


def write_file(filename, data):
    with open(dir_path + filename, 'w') as f:
        for item in data.items():
            f.write(item[key_index] + ": " + item[value_index])
