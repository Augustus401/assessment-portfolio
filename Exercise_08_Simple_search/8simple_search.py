print("here are the list")
name = ["Jake","Zac","Lan","Ron","Sam","Dave"]
print(name)
looking_for = input('enter a name to search: ')
if looking_for in name:
    print(f"{looking_for} found in the list")
else:
    print(f"{looking_for} not found in the list")