"""
    1. Get a wordnet_id from each line in wordnet_id_to_fruit.txt,
    2. Get a page containing urls to images of that wordnet_id
    3. Put all those urls into database
    4. Repeat with the next wordnet_id from wordnet_id_to_fruit.txt
"""

import urllib.request
import os
import sys
import image_database


if os.path.isfile(image_database.DB_PATH):
    if input('Image database already exists. Are you sure you want to continue? (y/n): ') != 'y':
        sys.exit(0)

image_database.connect(reset=True)

# category type: 0=fruit, 1=veg, 2=other
for category_type, file_name in enumerate(['utils/wordnet_id_to_fruit.txt', 'utils/wordnet_id_to_vegetables.txt']):
    file = open(file_name, 'r')
    for line in file:
        wordnet_id, name = line.strip().split(maxsplit=1)
        
        image_database.add_category(wordnet_id, name, category_type)
        
        print('downloading:', wordnet_id, '(' + name + ')')
        
        response = urllib.request.urlopen('http://image-net.org/api/text/imagenet.synset.geturls?wnid=' + wordnet_id)
        for response_line in response:
            url = response_line.decode().strip()
            if len(url) > 0:
                image_database.add_url(url, category_id=wordnet_id)
        
        image_database.commit()
    file.close()

image_database.close()
