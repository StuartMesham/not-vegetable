import urllib.request
import os
import sys

file = open(os.path.join(sys.argv[1], 'group_codes.txt'), 'r')

for line in file:
	code = line.split()[0]
	print(code)

	url_file = open(os.path.join(sys.argv[1], 'image_urls', code+'.txt'), 'w')

	response = urllib.request.urlopen('http://image-net.org/api/text/imagenet.synset.geturls?wnid='+code)
	for response_line in response:
		url = response_line.decode().strip()
		if len(url) > 0:
			url_file.write(url + '\n')

	url_file.close()
file.close()