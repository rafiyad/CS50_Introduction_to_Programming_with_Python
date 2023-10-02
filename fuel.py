while True:
    try:
        call=input("Fraction: ")
        name=call.split("/")
        x=int(name[0])
        y=int(name[1])
        if y==0:
            continue
        elif x>y:
            continue

    except ValueError:
        pass
    else:
        #print(x,y)
        result=round((x/y)*100)
        if result>=99:
            print("F")
        elif result<=1:
            print("E")
        else:
            print(result,"%",sep="")
        break