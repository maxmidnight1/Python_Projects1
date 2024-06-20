name = input ("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who")

"""
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")


if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")

if name == "Harry" or name == "Hermione"  or name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""