import os
# import argparse
import sys
import json


# def args_parser():
#     """
#     args_parser()
#     Parses positional arguments
#     """
#     parser = argparse.ArgumentParser(description='main.py parser')
#     parser.add_argument("path_to_data", type=str, help='Path to data')
#     return parser.parse_args()


"""
dict
  list:
    dict:
      items
  dict:
    items

ec_fun_to_go_through_data(data, word):
	if isinstance(data, dict):
		for elem in data.keys():
			if elem == word:
				found
		if found:
			print(found!)
			rec_fun_to_go_through_data(data[word], word)
"""


def get_labels_from_data(data):
    ans = ""
    for i, elem in enumerate(data):
        if i != len(data)-1:
            ans += f" |-> {elem}\n"
        else:
            ans += f" --> {elem}\n"
    print(ans)


def parse_data(filename: str):
    """
    Function that parses json file
    and finds class code
    """
    data = json.load(open(filename))
    # get_labels_from_data(data[idx])
    # ans = {}
    # ans = json.dumps(ans, indent=4, ensure_ascii=False)
    return data


def process_data(data, idx):
    found = False
    is_list = False
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
                        f' ! You can choose certain key between' +
                        f' {get_labels_from_data(data[idx].keys())}:')
        process_data(data[idx], new_idx)

    if isinstance(data[idx], list):
        new_idx = input(f' ! Key "{idx}" leads to a list\n' +
                        f' ! You can choose certain index in range 0-{len(data[idx])-1}:')
        process_data(data[idx], new_idx)
    return data[new_idx]


def main():
    """
    Main function
    """
    import time
    now = time.time()
    # args = args_parser()
    # path_to_data = args.path_to_data
    while 1:
        path_to_data = input('data location: ')
        to_find = input('Key to find: ')
        if not os.path.isfile(path_to_data):
            print(f" ! Usage: {sys.argv[0]} <argument>\n" +
                  " ! path_to_data should be an existing file!")
        else:
            print(process_data(parse_data(path_to_data), to_find)[0])
    # if print_time:
    # print(f' # Time: {time.time() - now} sec.')
    print('\n # Success!')


if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())
    main()
