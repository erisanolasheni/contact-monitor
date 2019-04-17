import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Monitor app streams.')
parser.add_argument('--column',
                    help='an option for the table column')
parser.add_argument('--max_count', 
                    help='an option for the maximum count')
parser.add_argument('--max_value', 
                    help='an option for the maximum value')

args = parser.parse_args()

# print(args.column, args.max_count, args.max_value)

limit_count = 0
max_count = int(args.max_count)
max_value = int(args.max_value)
columns = int(args.column)
while True:
    input_val = str(input()).strip()

    # first remove unnecessary spaces
    input_val = re.sub(r'\W+', ' ',input_val)

    # split to arrays to get the number of columns
    input_val_arr = input_val.split(' ')    
    try:
        # check if the value has passed the max_value
        if int(input_val_arr[columns-1]) > max_value:
            limit_count += 1

        if limit_count > max_count:
            print('Gone out!!!')
            limit_count = 0
    except:
        pass
    