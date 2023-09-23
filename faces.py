#input function
def main():
    text=input("Enter your text: ")
    myemogi(text)

#replacing function
def myemogi(name):
    print(f"{name}".replace(":)","🙂").replace(":(","🙁"))


#calling main to run
main()