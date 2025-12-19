def hashPass(password):


    allowedNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    allowedLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    allowedSymbols = ["#", "*", "$"]


    password = list(password.lower())
    for i in range(len(password)):
        if any(password[i] == num for num in allowedNums):
            if password[i] == allowedNums[0]:
                password[i] = "!"
            elif password[i] == allowedNums[2]:
                password[i] = ")"
            elif password[i] == allowedNums[4]:
                password[i] = "&"
            elif password[i] == allowedNums[7]:
                password[i] = "+"
            elif password[i] == allowedNums[9]:
                password[i] = "("

        elif any(password[i] == num for num in allowedLetters):
            if password[i] == allowedLetters[0]:
                password[i] = "0"
            elif password[i] == allowedLetters[2]:
                password[i] = "9"
            elif password[i] == allowedLetters[4]:
                password[i] = "8"
            elif password[i] == allowedLetters[6]:
                password[i] = "7"
            elif password[i] == allowedLetters[8]:
                password[i] = "6"
            elif password[i] == allowedLetters[10]:
                password[i] = "5"
            elif password[i] == allowedLetters[12]:
                password[i] = "4"
            elif password[i] == allowedLetters[14]:
                password[i] = "3"
            elif password[i] == allowedLetters[16]:
                password[i] = "2"
            elif password[i] == allowedLetters[18]:
                password[i] = "1"
            elif password[i] == allowedLetters[20]:
                password[i] = "_"
    
        elif any(password[i] == num for num in allowedSymbols):
            if password[i] == allowedSymbols[0]:
                password[i] = "go"
            elif password[i] == allowedSymbols[1]:
                password[i] = "rden"
            elif password[i] == allowedSymbols[2]:
                password[i] = "freeman"

    return password



userRoles = {
    "alice": "admin",
    "bob": "user",
    "charlie": "moderator",
    "diana": "user",
    "larisa": "user",
    "zhenechka": "admin"
    }

userPass = {
    "alice": ['2', '3', 'd', 'f', 'j', '5', '5', '1', '5', 'l', '1', '9', 'rden', '0', 'd', '5'],
    "bob": ['1', '2', '5', '3', '6', '1', '5', 'f', '7', '3', '7', '3', '7', '3', 'r', 'd', '8', 'n'],
    "charlie": ['2', 'w', '8', 'r', 't', 'y', '6', '1', '2', '3'],
    "diana": ['1', '0', 'd', '3', '8', '3', '2', '7', 't'],
    "andrey": ['0', '8', 'z', '0', '5', '4', '6'],
    "larisa": ['v', '3', 'r', '3', 'n', '8', 'n', '3', '5'],
    "zhenechka": ['0', 'n', 'd', 'r', '8', 'y', 'l', '3', 'v', '8', 'r']
    }

users = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana", 
    5: "Andrey",
    6: "Larisa",
    7: "Zhenechka"
    }



def checkRoles(userLogin):
    if userLogin.lower() in userRoles.keys():
        print(f"Role: {userRoles[userLogin.lower()]}")

    moderator = "moderator"
    if any(moderator == modRole for modRole in userRoles.values()):
        print(f"{moderator.capitalize()} exists in the system.")
    else:
        print(f"No {moderator.capitalize()} in the system.")


def checkAndAuth(userLogin):
    if any(userLogin.lower() == value.lower() for value in users.values()):
        userPassword = input("Password: ")
        if hashPass(userPassword) == userPass[userLogin.lower()]:
            print(f"Welcome, {userLogin.capitalize()}!")
            checkRoles(userLogin)
        else:
            print("Auth error.")
        return userPassword
    else: 
        print("User not found.") # add registration function call


userLogin = str(input("Login: "))
checkAndAuth(userLogin)