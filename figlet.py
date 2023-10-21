from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv)>1:
    if (sys.argv[1] =="-f" or sys.argv[1] =="--font") and sys.argv[2] in figlet.getFonts():
            ufont=sys.argv[2]

    elif sys.argv[1] !="-f" or sys.argv[1] !="--font" or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

else:
    ufont=random.choice(figlet.getFonts())

s=input("Enter value : ")
figlet.setFont(font=ufont)
print(f"Output: {figlet.renderText(s)}")