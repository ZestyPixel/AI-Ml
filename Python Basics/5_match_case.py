a = input("Enter colour: ")

match(a):
    case "Green":
        print("Color is green")
    case "Blue":
        print("Colour is blue")
    case _:
        print("Incorret input")
