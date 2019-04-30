import sys
import os
import glob
from PIL import Image

if len(sys.argv) < 2:
    print('usage: python3 utils/remove_non_images.py data/strawberry')
    sys.exit(0)

files = glob.glob(os.path.join(sys.argv[1], '*'))

for file in files:
    try:
        Image.open(file)
    except:
        os.remove(file)
