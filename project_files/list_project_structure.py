"""
D. (2012, March 16). List directory tree structure in python? Retrieved April 24, 2019,
    from https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

"""

import os
import sys
import datetime

startpath = sys.argv[1]
file = open(os.path.join(startpath, "project_file_structure.txt"), "w+")
currentDT = datetime.datetime.now()
file.write("Last Updated: " + str(currentDT) + "\n\n")
for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    indent = ' ' * 4 * level
    file.write('{}{}/\n'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        if f[0] == "n" and f[-4:] == ".txt":
            file.write('{}{}\n'.format(subindent, "-----files omitted for brevity-----"))
            break
        else:
            file.write('{}{}\n'.format(subindent, f))

