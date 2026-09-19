available_seats = 5
while available_seats > 0:
    print(f"So available seats are {available_seats}...")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    if booking == "yes":
        s = input("No. of seats: ")
        if not s.isdigit():
            print("Please enter a valid number of seats.\n")
            continue
            
        s = int(s)
        if s <= 0:
            print("Please enter at least 1 seat.\n")
            continue
            
        elif s > available_seats:
            print(f"Sorry, only {available_seats} seats are available.\n")
            continue

        available_seats = available_seats - s
        print(f"{s} seat(s) booked successfully.")
        print(f"{available_seats} seats are remaining.\n")
    elif booking == "no":
        print("No booking made.")
        break
    else:
        print("Please enter only 'yes' or 'no'.\n")
if available_seats == 0:
    print("No seats are available for booking.\n")

print("Have a great Day!")
print("Thank you for choosing our travels")