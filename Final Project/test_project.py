import pytest
from project import welcome_page, view_available_rooms, book_room, check_out_room


def main():
    test_welcome_page()
    test_view_available_rooms()
    test_book_room()
    test_check_out_room()
    test_welcome_page_invalid_input()


def test_welcome_page(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert welcome_page() == "1"
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert welcome_page() == "2"


def test_welcome_page_invalid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert welcome_page() is None
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    assert welcome_page() is None

def test_view_available_rooms():
    hotel_rooms = [101, 102, 103, 104, 105]
    booked_rooms = []
    assert view_available_rooms(hotel_rooms, booked_rooms) == hotel_rooms


def test_book_room():
    # Test case 1: Book a room
    booked_rooms = []
    room_number = 101
    book_room(room_number, booked_rooms)
    assert booked_rooms == [101]

    # Test case 2: Book another room
    room_number = 102
    book_room(room_number, booked_rooms)
    assert booked_rooms == [101, 102]

def test_check_out_room():
    booked_rooms = [101, 102, 103]
    room_number = 102
    check_out_room(room_number, booked_rooms)
    assert booked_rooms == [101, 103]

    room_number = 101
    check_out_room(room_number, booked_rooms)
    assert booked_rooms == [103]


if __name__ == "__main__":
    main()
