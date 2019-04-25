import sys






def my_function(string):
    print(string)

# To run from the command line:
# python3 clean_data.py my_function my_parameter

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
