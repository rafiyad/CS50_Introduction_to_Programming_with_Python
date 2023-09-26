name=str(input("Enter your greeting: ")).lower().strip()

if "hello" in name:
    print("$0")
elif "h" in name[0] and name !="hello":
    print("$20")
else:
    print("$100")
