#!/usr/bin/env python

import argparse
import subprocess
import os
import glob 

def find_files(start_dir, filter_name, filter_type, action):
    # os.walk() generates file names in a directory tree 
    # It returns a generator of tuples containing three values: current directory path,
    # list of subdirectories in that directory and a list of filenames in that directory
    # For each iteration, line 16 unpacks the tuple into three variables: 
    # root, _, and files for the current directory path, list of subdirectories 
    # in that directory (which we ignore by convention, hence the underscore _), 
    # and a list of filenames in that directory
    for root, dirs, files in os.walk(start_dir):
        # iterating through all the files in the current directory.
        for item in dirs + files:
            item_path = os.path.join(root, item)

            
            # Apply filter by type (file or directory)
            if filter_type == 'd' and not os.path.isdir(item_path):
                continue
                # If true skip the current file and proceed to the next one
            elif filter_type == 'f' and not os.path.isfile(item_path):
                continue
                # If true skip the current file and proceed to the next one


            # Apply filter by -name
            # checks if each file's name matches the specified pattern. 
            # If it doesn't match, the file is skipped, 
            # only files with names matching the pattern are considered in the search. 
            # If no -name filter is provided, all files are included in the search
            if filter_name and not glob.fnmatch.fnmatch(item, filter_name):
                continue

            # Perform action
            if action == '-print':
                print(item_path)
                # if the action string starts with the characters 'exec '
            elif action.startswith('exec '):
                # the command to be executed on each found file
                # extract the <command> part of the action by taking a substring of the action string 
                # from the 6th character onward to effectively removes the -exec prefix.
                # replaces any instance of {} with the name of the file
                command = action[5:].replace('{}', item_path)
                # command string as the command to execute and the 
                # shell=True argument to run the command in a shell environment.
                subprocess.call(command, shell=True)

            if action == '-print' and filter_type == 'd' and os.path.isdir(item_path):
                print(item_path)


# Main function to parse command-line arguments and initiate the search
def main():
    parser = argparse.ArgumentParser(description="A basic find tool")
    parser.add_argument("start_dir", help="Where to start searching")
    parser.add_argument("-name", help="Filter by file name")
    parser.add_argument("-type", help="Filter by file type (d for directory, f for file)")

    # Make the -action argument optional with a default value of 'print'
    parser.add_argument("-print", action="store_true", help="Print found files")
    parser.add_argument("-exec", help="Execute a command on found files")


    args = parser.parse_args()
    start_dir = args.start_dir
    filter_name = args.name
    filter_type = args.type
    

    # Check if the starting directory exists
    # start_dir is the mentioned path to start the search at from
    if not os.path.exists(start_dir):
        print(f"Directory '{start_dir}' does not exist.")
        return

    # determine the action to perform
    if args.print:
        find_files(start_dir, filter_name, filter_type, '-print')
    elif args.exec:
        find_files(start_dir, filter_name, filter_type, f'exec {args.exec}')
    else:
        print("Invalid action. Use -print or -exec.")




if __name__ == "__main__":
    main() 