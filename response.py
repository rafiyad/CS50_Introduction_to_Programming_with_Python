import validators

# pip install validators


def main():
    address=input("What's your email address? ")
    if validators.email(address):
        print("Valid")
    else:
        print("Invalid")




if __name__ == "__main__":
    main()
