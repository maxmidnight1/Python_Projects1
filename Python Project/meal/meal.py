def main():
    time = input("Enter the time (e.g., 7:30 AM or 13:15): ").strip()
    hours = convert(time)
    print(f"Converted time in decimal hours: {hours}")  # Debugging statement
    if is_breakfast_time(hours):
        print("It's breakfast time")
    elif is_lunch_time(hours):
        print("It's lunch time")
    elif is_dinner_time(hours):
        print("It's dinner time")

def convert(time):
    # Handle 12-hour time format
    if "AM" in time or "PM" in time:
        time, period = time.split()
        hours, minutes = map(int, time.split(':'))
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
    # Handle 24-hour time format
    else:
        hours, minutes = map(int, time.split(':'))credits
    return hours + minutes / 60

def is_breakfast_time(hours):
    return 7 <= hours <= 8

def is_lunch_time(hours):
    return 12 <= hours <= 13

def is_dinner_time(hours):
    return 18 <= hours <= 19

if __name__ == "__main__":
    main()
