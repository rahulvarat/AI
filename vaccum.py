
rooms = {"A": "dirty", "B": "dirty"}
location = "A"

while True:
    print("\nlocation", location)

    if rooms[location] == "dirty":
        print("percept: dirty")
        print("Action: Suck")
        rooms[location] = "clean"

    else:
        print("percept: clean")

        if rooms["A"] == "clean" and rooms["B"] == "clean":
            print("both rooms are clean")
            print("goal achieved")
            break

        if location == "A":
            print("action move to right")
            location = "B"
        else:
            print("action move to left")
            location = "A"
