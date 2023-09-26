def main():
    timein=input("What time is it? ")
    x=convert(timein)

    if convert(timein)>=7.00 and convert(timein)<=8.00:
        print("breakfast time")
    elif convert(timein)>=12.00 and convert(timein)<=13.00:
        print("lunch time")
    elif convert(timein)>=18.00 and convert(timein)<=19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    t=int((minutes.rstrip("p.m.").rstrip("a.m.")))
    if "p.m." in minutes:
        return (int(hours)+int(t)/60)+12
    return (int(hours)+int(t)/60)


if __name__ == "__main__":
    main()