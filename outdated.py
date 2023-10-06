months=["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    try:
        name=input("Date: ").strip()
        if "," in name:
            item=name.split(" ")
            if item[0] in months:
                x=(months.index(item[0]))+1
                y=int(item[1].rstrip(","))
                if y>31:
                    continue
                print(f"{item[2]}-{x:02}-{y:02}")
                break

        elif "/" in name:
            item=name.split("/")
            x=int(item[0])
            if x>12:
                continue
            y=int(item[1])
            if y>31:
                continue
            print(f"{item[2]}-{x:02}-{y:02}")
            break
    except ValueError:
        pass
