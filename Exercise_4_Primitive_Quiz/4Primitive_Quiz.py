def the_capitals():
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "United Kingdom": "London",
        "italy": "Rome",
        "Russia": "Moscow",
        "Spain": "Madrin",
        "Portugal": "Lisbon",
        "Switzerland": "Bern",
        "Netherland": "Amsterdam",
        "Greece": "Athens"
    }
    print("answer this question")
    for country, capital in capitals.items():
        answer = input(f"what is the capital of {country}?:")
        if answer.strip().lower() == capital.strip().lower():
            print("Correct")
        else:
            print(f"Incorrect its {capital}")

the_capitals()