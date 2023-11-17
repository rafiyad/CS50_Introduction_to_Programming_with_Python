
def main():
    fraction= input("Fraction: ")
    fraction_converted=convert(fraction)
    output=gauge(fraction_converted)
    print(output)


def convert(fraction):
    while True:
        try:
            #call=input("Fraction: ")
            nam1, nam2=fraction.split("/")
            x=int(nam1)
            y=int(nam2)
            result=x/y
            if result <=1:
                percent=result*100
                return percent
            else:
                fraction= input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage>=99:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        percentage=int(percentage)
        return f"{percentage}%"


if __name__ == "__main__":
    main()
