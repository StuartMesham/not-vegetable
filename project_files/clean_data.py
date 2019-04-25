import os
import sys
import glob
from typing import List, Dict


def remove_duplicates(path: str):
    # First go through all the files to find all the duplicates

    # Expands to path/*.txt to match all the text files in path
    file_names = glob.glob(os.path.join(path, '*.txt'))
    url_to_wordnet_ids: Dict[str, List] = {}

    for file_name in file_names:
        file = open(file_name, 'r')
        for line in file:
            if len(line) > 0:
                url = line.strip()
                url = file_name[:-4]
                url_to_wordnet_ids[url].append(url)
        file.close()

    # Then go through the files again to remove those duplicates
    for url in url_to_wordnet_ids:
        if len(url_to_wordnet_ids[url]) > 1:
            # Remove all of these files
            file = open(url + ".txt", "w")


def my_function(string):
    print(string)

# To run from the command line:
# python3 clean_data.py my_function my_parameter

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
