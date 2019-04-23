import os
import glob

file_names = []

groups = ['fruit', 'vegetables']
URLs = [set(), set()]
duplicates = [[], []]

for i in range(len(groups)):
	file_names = glob.glob(os.path.join(groups[i], 'image_urls', '*.txt'))

	for file_name in file_names:
		file = open(file_name, 'r')
		for line in file:
			if len(line) > 0:
				url = line.strip()
				if url in URLs[i]:
					duplicates[i].append(url)
				else:
					URLs[i].add(url)
		file.close()

	print(len(duplicates[i]), 'duplicates within', groups[i])

conflicts = URLs[0].intersection(URLs[1])
print(len(conflicts), 'images containing both fruit and vegetables:')

for conflict in conflicts:
	print(conflict)

print(len(URLs[0].symmetric_difference(URLs[1])), 'usable images')