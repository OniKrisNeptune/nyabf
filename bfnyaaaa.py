for i in list(input()):
    match i:
        case "n": print("+", end="")
        case "y": print("-", end="")
        case "a": print(",", end="")
        case "~": print("[-]", end="")
