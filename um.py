import re
import sys


def main():
    text="um, hello, um, world"
    print(count(text))
    #print(count(input("Text: ")))


def count(s):
    #count=0
    found=re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(found)

    #for i in found:
       # if i=="um":
           # count+=1
    #return count



if __name__ == "__main__":
    main()
