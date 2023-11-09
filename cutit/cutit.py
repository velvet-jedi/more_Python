#!/usr/bin/env python

import argparse
import sys




# perform the cut
def cut_text(input_stream, output_stream, delimiter, field_range):
    for line in input_stream:
        line = line.strip()
        if delimiter:
            tokens = line.split(delimiter) 
            # splits the line into a list of tokens using the specified delimiter. 
            # For example, if the delimiter is a space character (' '), it will split the line into words.

            
            line = delimiter.join(tokens[field_range[0]:field_range[1] + 1])
        output_stream.write(line + '\n')


def main():
    
# deal with arguments/options 
    
    # create an object of type ArgumentParser
    parser = argparse.ArgumentParser(description="Cut utility clone to remove sections line by line using delimiters")

    parser.add_argument("input_file", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="Input Files")
    # nargs='?' makes specifying a file as input optional
    # or read from standard input (stdin) if no file name is provided. 
    # This is used to handle both explicit file inputs and piped inputs.
    # the argument should be a file object that can be opened for reading
    parser.add_argument('-b', '--delimiter', help="Selected bytes to remove (e.g., 1-5,7-9)")
    parser.add_argument('-f', '--fields', help="Field delimiter Field range (e.g., 5-7)")
    
    
    # interact with your script from the command line.
    # parsed arguments are stored in args as python objects
    args = parser.parse_args()
    field_range = None

    if args.fields:
        # For example, if args.fields is "5-7", it will split into ["5", "7"]
        # After splitting the field range, it converts the substrings to integers
        start, end = map(int, args.fields.split('-'))
        #  0-based index.
        field_range = (start - 1, end - 1)
    
    cut_text(args.input_file, sys.stdout, args.delimiter, field_range)


if __name__ == "__main__":
    main()