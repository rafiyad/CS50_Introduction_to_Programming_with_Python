def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")


def dollars_to_float(d):
    # TODO
    c=float(d.removeprefix("$"))
    return c


def percent_to_float(p):
    # TODO
    d=float(p.removesuffix("%"))
    return d/100


main()
