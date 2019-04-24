
"""
    Once off tool that Stu used to speed up making the group_codes.txt files
    for fruit and veggie ImageNet wnids (WordNet ids)
"""
import sys

if len(sys.argv) < 2:
    print('usage: python3 tool_to_create_group_codes.py vegetables/vegetable_names.txt')
    sys.exit(0)

source = open('wnid_to_word.txt', 'r')
destination = open(sys.argv[1], 'r')

lines = source.readlines()


def grep(needle):
    for line in lines:
        if needle.lower() in line.lower():
            print(line, end='')


for line in destination:
    name = line.strip()
    print(name)
    grep(name)
