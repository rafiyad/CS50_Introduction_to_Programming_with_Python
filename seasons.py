from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dob=input("Date of Birth: ")
    try:
        year, month, day = dob_check(dob)
        date_of_birth=date(int(year), int(month), int(day))
        present_date=date.today()

        age = present_date-date_of_birth
        out_minutes=age.days*24*60

        output=p.number_to_words(out_minutes, andword="")
        print(output.capitalize() + " minutes")


    except:
        sys.exit("Invalid date")


def dob_check(i):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",i):
        year, month, day=i.split("-")
        return year, month, day


#def leap_year(y, m, d):



if __name__ == "__main__":
    main()
