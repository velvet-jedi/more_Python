#!/usr/bin/env python

import argparse
import re

def sed_replace(pattern, replacement, filename, use_regex=False, full_expression=None):
    with open(filename, 'r') as file:
        text = file.read()

    if full_expression:
        # ./sed.py -f "s/quick/slow/g" sample.txt
        # If a full_expression is provided, split it into separate sed 
        # commands using semicolons.

        sed_commands = full_expression.split(';')

        # Iterate through each sed command.
        for command in sed_commands:
            
    # Check if the command starts with "s/"; this indicates a valid sed replacement command.
            if command.startswith("s/"):

            # Split the command using '/' as the separator, which should give us three or more parts:
            # 0: Empty
            # 1: The sed pattern to search for
            # 2: The sed replacement to replace the pattern with

                parts = command.split('/')
                if len(parts) >= 3:
                    # Extract the sed pattern (parts[1]) and sed replacement (parts[2]) from the command.
                    sed_pattern, sed_replacement = parts[1], parts[2]
                    # Use re.sub to apply the sed_pattern and sed_replacement to modify the text.
                    text = re.sub(sed_pattern, sed_replacement, text)
                else:
                    # If the command doesn't have enough parts, it's considered invalid.
                    print(f"Invalid sed command: {command}")

    elif use_regex:
        text = re.sub(pattern, replacement, text)
    else:
        # usage
        # ./sed.py -p "RAAM" -r "RAM" sample_in.txt
        text = text.replace(pattern, replacement)

    with open(filename, 'w') as file:
        file.write(text)

def main():
    parser = argparse.ArgumentParser(description='Sed like tool')
    parser.add_argument("-p", "--pattern", help='Pattern to search for')
    parser.add_argument("-r", "--replacement", help='Pattern to replace it with')
    
    # argument attribute 
    parser.add_argument("-e", "--regex", action="store_true" , help='Expression')
    parser.add_argument("-f", "--full_expression", help='Full sed expression')
    parser.add_argument("filename", help='File to modify')

    args = parser.parse_args()

    if args.full_expression:
        sed_replace(None,None, args.filename, full_expression=args.full_expression)
    elif args.pattern and args.replacement:
        sed_replace(args.pattern, args.replacement, args.filename, use_regex=args.regex)
    else:
        print("Give pattern and string for replacement in a file")

if __name__ == '__main__':
    main()