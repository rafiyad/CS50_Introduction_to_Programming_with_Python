name=input("Input: ")
vowels = "aeiouAEIOU"
print("Output: ",end="")

for c in name:
    print(c.lstrip(vowels),end="")

print()
