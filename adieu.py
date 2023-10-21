import inflect

p = inflect.engine()

li=[]
while True:
    try:
        name=input("enter ")
        li.append(name)
    except EOFError:
        break

mylist=p.join(li)
print("Adieu, adieu, to",mylist)