name=input("camelCase: ")

print("snake_case: ",end="")
for c in name:
    print(c.replace("F","_f").replace("N","_n"), end="")

print()