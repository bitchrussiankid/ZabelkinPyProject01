def pluralForm(item: str, quantity: int) -> str:
    if quantity == 1:
        return item
    else:
        return item + "s"

item = "book"
price = 9.99
quantity = 3

print(f"Total for {quantity} {pluralForm(item, quantity)}: ${(price * quantity): .2f}")