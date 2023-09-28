deu=50
print(f"Amount Due: {deu}")

while deu>0:
    insert=int(input("Insert Coin: "))
    if insert==25 or insert==10 or insert==5:
        deu=deu-insert
    if deu >0:
        print(f"Amount Due: {deu}")

change=abs(deu)
print(f"Change Owed: {change}")