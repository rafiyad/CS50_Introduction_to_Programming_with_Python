import sys
import csv
from tabulate import tabulate

def main():
    check_argument()
    row=[]
    table=[]
    try:
        with open (sys.argv[1]) as file:
            for line in file:
                row.append(line.rstrip().split(","))

        table=row[1:]
        headers=row[0][0],row[0][1],row[0][2]
        print(tabulate(table,headers,tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_argument():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

def check_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
