def converterToNumber(number):
    if "." in number:
        number = float(number)
        return number
    elif "," in number:
        print("Incorrect number!")
        return "error"
    else:
        number = int(number)
        return number