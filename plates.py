def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and 3<len(s) and len(s)<7:
            return True

    else:
        return False


main()

"""
# checking the input is alphabetic 1st 2 letter and range betwwen 4 to 6
if name[:2].isalpha() and 3<len(name) and len(name)<7:
    # here checking is the number between alphabet 
    if name[-3:].isnumeric() or name[-2:].isnumeric():
        print(name)
        print("Valid")

else:
    print("Invalid")
"""