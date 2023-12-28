from tabulate import tabulate

def main():
    hotel_rooms=("A1001","A1002","A1003","B2001","B2002","B2003","C3001","C3002","C3003")
    booked_rooms=["A1002","B2001","B2002","C3003"]


    print("Welcome To Hotel Relax 🏰 ")
    while True:
        action=welcome_page()
        if action=="1":
            rooms=view_available_rooms(hotel_rooms, booked_rooms)
            print(f"{rooms} are available for booking 🏖️".replace("[","").replace("]","").replace("'",""))

        elif action=="2":
            booked=input("Enter room number for check in : ")
            if booked in hotel_rooms and booked not in booked_rooms:
                print(f"You have booked room {booked}. Enjoy your stay.⛲")
                book_room(booked, booked_rooms)
            else:
                print("Please enter right room number")


        elif action=="3":
            check_out=input("Enter room number for check out : ")
            if check_out in booked_rooms:
                check_out_room(check_out, booked_rooms)
                print(f"You have checked out from {check_out}. Have a greate day.🧭")
            else:
                print("Please enter right room number")

        elif action=="4":
            print("Thank you, have a good day.🌄")
            break
        else:
            print("Please select from 1 to 4 ")



def welcome_page():
    instructions = [{"Key": "1", "Action": "View Available Rooms"},
                    {"Key": "2", "Action": "Check in Rooms"},
                    {"Key": "3", "Action": "Check Out"},
                    {"Key": "4", "Action": "Exit"}]


    print(tabulate(instructions, headers="keys", tablefmt="grid"))
    action = input("Please select your key to enter (From 1-4): ")
    if action in ["1", "2", "3", "4"]:
        return action



def view_available_rooms(hotel_rooms, booked_rooms):
    available_rooms = list(set(hotel_rooms) - set(booked_rooms))
    return available_rooms


def book_room(room_number, booked_rooms):
    booked_rooms.append(room_number)


def check_out_room(room_number, booked_rooms):
    if room_number in booked_rooms:
        booked_rooms.remove(room_number)


if __name__ == "__main__":
    main()
