#!/usr/bin/env python

import argparse
import re
import glob 

# Define the script version
VERSION = '1.0'


def grep(pattern, file_path):
    flag = 'false'

    # we use glob.glob to expand the file paths matching the file_path pattern
    files = glob.glob(file_path)
    for file in files:
        try:
            with open(file, "r") as file_obj:
                lines = file_obj.readlines()
        # The enumerate() iterates over the lines list and return both the 
        # line number and the line itself. The line numbering should start from 1
                for line_number, line in enumerate(lines, start=1):
                    if re.search(pattern, line):
                        flag = 'true'
                        print(f"{file_path}:{line_number}")
                
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        
    if not flag:
        print("No matches")


    




def main():
    parser = argparse.ArgumentParser(description="A copy of grep utility")

    # Define the various flags
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}', help="Display the version of grepit")
    

    # Define positional arguments
    parser.add_argument("pattern", help="Give the pattern (Regular Expression))")
    parser.add_argument("file_path", help="Where to look at for the pattern match")    
    
    

    args = parser.parse_args()
    grep(args.pattern, args.file_path)
    return


if __name__ == "__main__":
    main()
