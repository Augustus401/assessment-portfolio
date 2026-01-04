UN = "admin"
CORRECT = "12345"
MAX = 5

for attempt in range(1, MAX + 1):
    name = input("Enter name: ")
    pw = input(f"Enter password: ")

    if pw == CORRECT and name == UN:
        print(f"welcome {name}")
        break
    else:
        print("Try again")
else:
    print("failed to login")