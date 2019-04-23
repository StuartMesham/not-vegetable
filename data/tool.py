# once off tool that Stu used to speed up making the group_codes.txt files for fruit and veggie ImageNet wnids (WordNet ids)

import sys

if len(sys.argv) < 2:
	print('usage: python3 tool.py vegetables/vegetable_names.txt')
	sys.exit(0)

file1 = open('words.txt', 'r')
file2 = open(sys.argv[1], 'r')

lines = file1.readlines()


def grep(needle):
	for line in lines:
		if needle.lower() in line.lower():
			print(line, end='')



for line in file2:
	name = line.strip()
	print(name)
	grep(name)