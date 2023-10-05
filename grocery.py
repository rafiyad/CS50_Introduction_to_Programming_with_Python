
grodict={}
while True:
    try:
        item = input().upper()
        if item in grodict:
            grodict[item]=int(grodict[item]+1)
        else:
            grodict[item]=1
    except EOFError:
        for i in sorted(grodict):
            print(grodict[i],i)
        break