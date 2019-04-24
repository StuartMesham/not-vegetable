"""
    1. Get a wordnet_id from each line in wordnet_id_to_fruit.txt,
    2. Get a page containing urls to images of that wordnet_id
    3. Put all those urls into image_urls/<wordnet_id>.txt
    4. Repeat with the next wordnet_id from wordnet_id_to_fruit.txt

    TODO Autoformat all files
    TODO Rename Groupcodes.txt
"""

import urllib.request
import os
import sys

textfile_name = "wordnet_id_to_" + sys.argv[1] + ".txt"
file = open(os.path.join(sys.argv[1], textfile_name), 'r')

for line in file:
    wordnet_id = line.split()[0]
    print(wordnet_id)

    url_file = open(os.path.join(sys.argv[1], 'image_urls', wordnet_id + '.txt'), 'w')

    response = urllib.request.urlopen('http://image-net.org/api/text/imagenet.synset.geturls?wnid=' + wordnet_id)
    for response_line in response:
        url = response_line.decode().strip()
        if len(url) > 0:
            url_file.write(url + '\n')

    url_file.close()
file.close()
