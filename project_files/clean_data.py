"""
# Usage
1. Run ```python3 clean_data.py remove_duplicates path```
    1.2 path =

"""
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
                wordnet_id = file_name[:-4]
                url_to_wordnet_ids[url].append(wordnet_id)
        file.close()

    # Then go through the files again to remove those duplicates
    for url in url_to_wordnet_ids:
        if len(url_to_wordnet_ids[url]) > 1:
            for wordnet_id in url_to_wordnet_ids[url]:
                file = open(wordnet_id + ".txt", "w")
                lines = file.readlines()
                lines.remove(url)
                file.writelines(lines)
                file.close()


def my_function(string):
    print(string)


# To run from the command line:
# python3 clean_data.py remove_duplicates path

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
