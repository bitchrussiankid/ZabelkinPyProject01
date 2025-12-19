def filling_list(count, users_list):
    for i in range(count):
        users_list.append(input("Enter your product: "))

    return users_list

count = 3
shopping_list = []
shopping_list = filling_list(count, shopping_list)

shopping_list[1] = "milk"
print(shopping_list)