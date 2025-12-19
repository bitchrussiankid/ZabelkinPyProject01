car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "blue"   
    }

keyCar = input("Enter the key: ").lower()

if keyCar in car.keys():
    print(car[keyCar])
else:
    print("Key not found")