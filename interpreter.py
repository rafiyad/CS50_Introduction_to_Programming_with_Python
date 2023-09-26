expression=input("Enter your numbers and arithmatic operator between them: ")
x, y, z = expression.split(" ")

if y== "+":
     print(float(int(x)+int(z)))
elif y=="-":
     print(float(int(x)-int(z)))
elif y=="*":
     print(float(int(x)*int(z)))
elif y=="/":
        print(float(int(x)/int(z)))