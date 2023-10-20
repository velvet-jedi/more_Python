#!/usr/bin/env python

import argparse
import shutil
import os
import glob 

# Define the script version
VERSION = "1.0"

def main():
    # Create an ArgumentParser object
    # uses the argparse module to create a command-line parser.
    # The ArgumentParser class
    # description is a string that will be displayed when the user requests 
    #   help or usage information for the script
    parser = argparse.ArgumentParser(description="Move files locally with moveit")

    
    # Define the version flag to display the script version
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}', help="show program's version")

    # Define the v flag to display verbose output
    parser.add_argument('-v', help="real time verbose output")    


    # Define the file argument for specifying files to move
    # nargs='+' specifies that the argument can take one or more values. 
    # The values will be stored in a list
    parser.add_argument('-file', nargs='+', help='Specify files to move')
    
    # Define the dir argument for specifying whole directory to move recursively
    parser.add_argument('-dir', nargs='+', help='Specify folder to move (recursive)')



    # Define the destination directory argument to specify destination location
    parser.add_argument('-dest', required=True, help='Specify the destination directory')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Ensure the destination directory exists
    if not os.path.isdir(args.dest):
        print(f"Error: '{args.dest}' is not a valid destination directory.")
        return


    selected_files = []
    if args.file:
        for pattern in args.file:
            matching_files = glob.glob(pattern)
            if not matching_files:
                print(f"Warning: No files match the pattern '{pattern}'")
            selected_files.extend(matching_files)

# Your script logic goes here

    # file move it logic
    
    for each_file in selected_files:
        if not os.path.exists(each_file):
            print(f"Error: The file '{each_file}' does not exist.")
            continue
        try:
            shutil.move(each_file, os.path.join(args.dest, os.path.basename(each_file)))
            if args.v:
                print(f"Moved '{each_file}' to '{args.dest}'")
        except Exception as e:
            print(f"Error moving '{each_file}': {str(e)}")

        

    # directory move it logic
    if args.dir:
        for each_dir in args.dir:
            try:
                shutil.move(each_dir, os.path.join(args.dest, os.path.basename(each_dir)))
                print(f"Moved '{each_dir}' to '{args.dest}'")
            except Exception as e:
                print(f"Error moving '{each_dir}': {str(e)}")
    

if __name__ == "__main__":
    main() 