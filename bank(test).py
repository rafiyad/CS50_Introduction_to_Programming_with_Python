
def main():
    name=input("Greeting: ")
    print(value(name))



def value(greeting):
    x=greeting.lower().strip()
    if "hello" in x:
        return 0
    elif x=="":
        return 100
    elif "h" in x[0] and x !="hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
