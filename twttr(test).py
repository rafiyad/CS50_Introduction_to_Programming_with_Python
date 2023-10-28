def main():
    name=input("Enter words: ")
    print(shorten(name))

def shorten(word):
   vowels = "aeiouAEIOU"
   filtered_word= ""
   for char in word:
       if not char in vowels:
           filtered_word +=char

   return filtered_word


if __name__=="__main__":
    main()
