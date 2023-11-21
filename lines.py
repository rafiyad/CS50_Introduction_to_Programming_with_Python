import sys
def main():
    check_argument()
    count=0
    #stat=[]
    try:
        file=open(sys.argv[1])
        lines=file.readlines()
        #print(lines)
        for line in lines:
            if check_lines(line)==False:
                count+=1
                #stat.append(line.strip())

        #print(stat)
        print(count)


    except FileNotFoundError:
        sys.exit("File does not exist")




def check_argument():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
