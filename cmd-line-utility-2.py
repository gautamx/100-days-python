
# execute from cmd line utility
# python "D:\Code\100-days-python\cmd-line-utility-2.py" my-file.txt -v -o cmd-out.txt -n 3

import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='My command line tool')
    
    # Add arguments
    parser.add_argument('filename', help='The file to process')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of iterations')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Access the values
    print(f"Processing {args.filename}")
    if args.verbose:
        print("Verbose mode enabled")
    if args.output:
        print(f"Output will be written to {args.output}")
    print(f"Will perform {args.number} iterations")

if __name__ == "__main__":
    main() 