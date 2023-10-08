import emoji

name=input("Input: ").strip()


if ":" in name[0]:
    #print("In if")
    print(emoji.emojize(f"{name}",language="alias"))

else:
    #print("in else")
    name=name.split(" ")
    print(emoji.emojize(f"Output: {name[0]} {name[1]}", language="alias"))