import random

while True:
    try:
        lv=int(input("Level: "))
        if lv>0:
            gs=(random.randint(1, lv))
            break
        else:
            pass

    except ValueError:
        pass

while True:
    try:
        guess=int(input("Guess: "))
        if guess>0:
            if guess>gs:
                print("Too large!")
            elif guess<gs:
                print("Too small!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass
