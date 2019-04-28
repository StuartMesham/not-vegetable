"""
# Usage
1. Run ```python3 clean_data.py remove_duplicates path```
    1.1 path = vegetables/image_urls
    1.2 path = fruit/image_urls
2. The program will remove all duplicated URLs from the files inside the given directory's path
"""
import os
import sys
import glob
from typing import List, Dict


def remove_duplicates(path: str):
    """
    To clean the data, make sure that all images only contain one type of fruit.

    Go through all the files regex matching n*.txt.
    For all those files, look in their contents and remove any URL that occurs more than once
    :param path: The path to search in
    :return: None
    """

    # First go through all the files to find all the duplicates

    # Expands to path/*.txt to match all the text files in path
    file_names = glob.glob(os.path.join(path, '*.txt'))
    url_to_filenames: Dict[str, List] = {}

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            for url in file:
                if len(url) > 0:
                    if url in url_to_filenames:
                        url_to_filenames[url].append(file_name)
                    else:
                        url_to_filenames[url] = [file_name]
    else:
        print("No files matching *.txt found in {}".format(path))

    # Remove all the urls that are not duplicates
    url_to_filenames = {url: filenames for url, filenames in url_to_filenames.items() if len(filenames) >= 2}

    # Let the user know what files are about to be removed
    for url in url_to_filenames:
        print("{}:\n\t[{}]".format(url.encode('utf-8').strip(), ", ".join(url_to_filenames[url]).encode('utf-8')))

    # Now go through the dictionary and remove all those URLs
    for url, filenames in url_to_filenames.items():
        for filename in filenames:
            with open(filename, "r+", encoding="utf8") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if line != url:
                        file.write(line)
                file.truncate()  # Remove all lines after the cursor
    print("Files removed from {}:{}".format(path, "File Removed: \t".join(url_to_filenames.keys()).encode('utf-8')))


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
