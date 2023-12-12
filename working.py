import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    found= re.search(r"^([0-9]+)(.([0-9]+))?.(AM|PM).to.([0-9]+)(:([0-9]+))?.(AM|PM)$", s)
    if found:
        times=found.groups()
        if int(times[0])>12 or int(times[4])>12:
            raise ValueError

        first_time=twenty_four_format(times[0], times[2], times[3])
        last_time=twenty_four_format(times[4], times[6], times[7])

        return f"{first_time} to {last_time}"

    else:
        raise ValueError

def twenty_four_format(hour, min, am_pm):
    if am_pm=="PM":
        if int(hour)==12:
            new_hour=12
        else:
            new_hour=int(hour)+12
    else:
        if int(hour)==12:
            new_hour=0
        else:
            new_hour=int(hour)

    if min==None:
        new_min=0
    else:
        new_min=int(min)
    if not -1<new_min<60:
        raise ValueError

    return f"{new_hour:02}:{new_min:02}"


if __name__ == "__main__":
    main()
