
"""
    Once off tool that Stu used to speed up making the wordnet_id_to_fruit.txt files
    for fruit and veggie ImageNet wnids (WordNet ids)
"""
import sys
import os
import urllib.request

if len(sys.argv) < 2:
    print('usage: python3 tool_to_create_group_codes.py utils/vegetable_names.txt')
    sys.exit(0)

if not os.path.isfile('data/wordnet_id_to_word.txt'):
    urllib.request.urlretrieve('http://image-net.org/archive/words.txt', 'data/wordnet_id_to_word.txt')

source = open('data/wordnet_id_to_word.txt', 'r')
destination = open(sys.argv[1], 'r')
print(sys.argv[1])

lines = source.readlines()


def grep(needle):
    for line in lines:
        if needle.lower() in line.lower():
            print(line, end='')


for line in destination:
    name = line.strip()
    print(name)
    grep(name)
