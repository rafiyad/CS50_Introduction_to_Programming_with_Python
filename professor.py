import random

def main():
    count=1
    score=0
    lv=get_level()

    while count<=10:
        x,y=generate_integer(lv)
        answer=game(x,y)
        if answer==True:
            score+=1
        count+=1
    print("Score:",score)


def game(x,y):
        err=1
        while err<=3:
            try:
                ans=int(input(f"{x} + {y} = "))
                if ans==(x+y):
                    return True
                else:
                    err+=1
                    print("EEE")
            except:
                err+=1
                print("EEE")

        print(f"{x} + {y} = {x+y}")
        return False


def get_level():
    while True:
        try:
            level=int(input("level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass

    return level

def generate_integer(level):
    if level ==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level ==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    else:
        x=random.randint(100,999)
        y=random.randint(100,999)

    return x,y



if __name__ == "__main__":
    main()
