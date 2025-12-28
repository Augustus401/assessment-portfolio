print("please enter your information")
name = input("enter your name: ")
hometown = input("enter your hometown: ")

while True:
    age = input("enter your age: ") #checking if its only Number
    if age.isdigit():
        age = int(age)
        if age > 0:
            break
        else:
            print("invalid age")
    else:
        print("must be a NUMBER and NO decimal place")

person_info = { #stores the info
    "name": name,
    "hometown": hometown,
    "age": age
}
print(person_info)


