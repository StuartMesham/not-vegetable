import sys


# To run from the command line:
# ```python3 clean_data.py myfunction```
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
