#!/usr/bin/env python

import argparse
import sys

def sort_lines(file_path, output_file, reverse, ignore_case, numeric_sort):
    # handle the input file if supplied
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    # handle the pipe if file not supplied
    else:
        lines = sys.stdin.readlines()

# sort the shiz
    # lambda function (anonymous function) named key_function
    # takes a single argument x, which represents a line of text. 
    # The purpose of it is to serve as the key function for sorting.
    key_function = lambda x: x.lower() if ignore_case else x
    sorted_lines = sorted(lines, reverse=reverse, key=key_function)

    if numeric_sort:
        # For numeric sorting, convert lines to floats
        sorted_lines = sorted(sorted_lines, key=lambda x: float(x) if x.strip().replace('.', '').isdigit() else x)

    # handle the output file if supplied
    if output_file:
        with open(output_file, 'w') as output:
            output.writelines(sorted_lines)
    else:
        for line in sorted_lines:
            # eliminate an unecessary newline at the end of each line in output
            print(line, end='')



def main():
    parser = argparse.ArgumentParser(description='Sort things like a pro')
    parser.add_argument("-o", "--output", help='Output to a file')
    parser.add_argument("-r", "--reverse", action='store_true' , help='Reverse the sort order')
    parser.add_argument("-f", "--ignore-case", action='store_true' , help='Treat upper and lower characters same')
    parser.add_argument("-g", "--numeric-sort", action='store_true' , help='Compare according to string numeric value')
    parser.add_argument("-file", nargs='?', help='Sort a file content or sort the output from standard input')

    # consolidate parsed arguments into a list
    args = parser.parse_args()

    # call the sort function on the arguments
    sort_lines(args.file, args.output, args.reverse, args.ignore_case, args.numeric_sort)

if __name__== '__main__':
    main()