month_days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
print("enter number of month")
print("between 1 to 12")
ask_month = int(input("answer here: "))
if ask_month in month_days:
    if ask_month == 2:
        leap_year = input("leap year?: ").strip().lower()
        if leap_year == "yes":
            print("February has 29 days.")
        elif leap_year == "no":
            print("February has 28 days.")
        else:
            print("invalid")
    else:
        print(f"this month has {month_days[ask_month]} days.")
else:
    print("invalid")