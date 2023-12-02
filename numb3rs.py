import re

def main():

    print(validate(input("IPv4 Address: ")))
    #print(validate("127.0.0.125"))



def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers=ip.split(".")
        for number in numbers:
            if int(number) <0 or int(number) >255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

