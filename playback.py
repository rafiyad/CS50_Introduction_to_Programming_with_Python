name = input("Please enter some text: ")
#creating list coming from input
name2 = name.split(" ")
#assigning empy string to store the split words
result=""
for words in name2:
    result += words +"..."

#print using rstrip to cut the right ... in the output 
print(result.rstrip("..."))