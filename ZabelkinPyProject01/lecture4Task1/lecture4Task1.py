def numberChecker(number):
    try:
        number = float(number)
        if number == 0:
            print("Zero")
        elif number > 0:
            print("Positive")
        else:
            print("Negative")
    except ValueError:
        print("Error: please enter a numeric value")
    except Exception as e:
        print("Unknown error")

usersNumber = input("Enter your number: ")
numberChecker(usersNumber)