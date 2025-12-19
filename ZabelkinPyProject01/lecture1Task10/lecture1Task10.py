def intChecker(x):
    if x % 2 == 0 and x > 0:
        return True
    else:
        return False

userInteger = int(input("Enter an integer: "))
print(f"Is the integer even and positive? {intChecker(userInteger)}")