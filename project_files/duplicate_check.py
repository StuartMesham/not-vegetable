"""
# Usage
Just run the program from the IDE
Go through all of our fruits and vegetables, and print out:
	* the number of fruit image urls that were referred to multiple times
	* the number of vegetable image urls that were referred to multiple times
	* the number of image urls that contain both fruits and vegetables
		* all the links of those images
	* the number of image urls which are not in both the fruits and the vegetables folders
"""

import os
import glob

file_names = []

groups = ['fruit', 'vegetables']
URLs = [set(), set()]
duplicates = [[], []]

for i in range(len(groups)): # For both the fruit and the veggies
	file_names = glob.glob(os.path.join(groups[i], 'image_urls', '*.txt'))

	for file_name in file_names:
		file = open(file_name, 'r')
		for line in file:
			if len(line) > 0:
				url = line.strip()
				if url in URLs[i]: # if url is already in the fruit's/veggie's set of urls, add it to the duplicates
					duplicates[i].append(url)
				else: # else add the url to the set of URLs
					URLs[i].add(url)
		file.close()

	print(len(duplicates[i]), 'duplicates within', groups[i])

conflicts = URLs[0].intersection(URLs[1])
print(len(conflicts), 'images containing both fruit and vegetables:')

for conflict in conflicts:
	print(conflict)

print(len(URLs[0].symmetric_difference(URLs[1])), 'usable images')