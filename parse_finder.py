"""
Easy parser
parse_finder.json
"""

# importing necessary modules
import os
import sys
import json


def get_labels_from_data(data):
    """
    Function that prints available keys
    """
    ans = "\n"
    for i, elem in enumerate(data):
        if i != len(data)-1:
            ans += f" |-> {elem}\n"
        else:
            ans += f" --> {elem}\n"
    print(ans)
    return ''


def parse_data(filename: str):
    """
    Function that parses json file
    """
    data = json.load(open(filename))
    return data


def process_data(data, idx):
    """
    Function that processes data
    """
    found = False
    new_idx = idx
    if isinstance(data, dict):
        for elem in data.items():
            if elem[0] == idx:
                found = True
        if not found:
            return f'Wrong key! choose one of those: {data.keys()}'
    if isinstance(data, list):
        if data[int(idx)] != None:
            is_list = True
        else:
            return f'Wrong key! choose one of 0-{len(data)-1}'
    try:
        idx = int(idx)
    except ValueError:
        pass
    if isinstance(data[idx], dict):
        new_idx = input(f' ! Key "{idx}" leads to a dict\n' +
                        f' ! You can choose certain key form above: {get_labels_from_data(data[idx].keys())}')
        process_data(data[idx], new_idx)
    elif isinstance(data[idx], list):
        new_idx = input(f' ! Key "{idx}" leads to a list\n' +
                        f' ! You can choose certain index in range 0-{len(data[idx])-1}: ')
        process_data(data[idx], new_idx)
    else:
        print(data[idx])
    return data


def main():
    """
    Main function
    """
    while 1:
        path_to_data = input('data location: ')
        to_find = input('Key to find: ')
        if not os.path.isfile(path_to_data):
            print(f" ! Usage: {sys.argv[0]} <argument>\n" +
                  " ! path_to_data should be an existing file!")
        else:
            process_data(parse_data(path_to_data), to_find)
    print('\n # Success!')


if __name__ == '__main__':
    main()
