import sys
import csv

def main():
    check_argument()
    output=[]

    try:
        with open(sys.argv[1], "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                names=row["name"].split(",")
                output.append({"first": names[1].lstrip(), "last": names[0], "house": row["house"]})


        with open (sys.argv[2], "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in output:
                writer.writerow({"first":row["first"], "last": row["last"], "house": row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


def check_argument():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
