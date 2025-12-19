def distributeCars(cars: dict, validCars: list) -> dict:
    carsShowroom = {}
    goToShowroomCars = []

    i = 1
    while i in range(len(cars) + 1):
        if any(cars[i].lower().startswith(car) for car in validCars):
            goToShowroomCars.append(cars[i].split(" "))
            
        i += 1


    for j in range(len(goToShowroomCars)):
        if goToShowroomCars[j][0] in carsShowroom.keys():
            carsShowroom[goToShowroomCars[j][0]] = carsShowroom[goToShowroomCars[j][0]] + ", " + goToShowroomCars[j][1]
        else:
            carsShowroom[goToShowroomCars[j][0]] = goToShowroomCars[j][1]

    return carsShowroom


cars = {
    1: "Toyota Corolla",
    2: "Toyota Camry",
    3: "Nissan Silvia",
    4: "Mercedes S-classe",
    5: "Mazda MX-5",
    6: "Mazda Miata",
    7: "Mazda 6",
    8: "Mercedes C-classe",
    9: "Audi RS3",
    10: "Changan UNI-V",
    11: "Geely Emgrand",
    12: "Volkswagen Scirocco"
    }

japanBrands = ["toyota", "nissan", "mitsubishi", "suzuki", "mazda"]
germanBrands = ["mercedes", "bmw", "audi", "volkswagen"]
chinaBrands = ["changan", "lifan", "geely"]

japanShowroom = distributeCars(cars, japanBrands)
print(japanShowroom)

germanShowroom = distributeCars(cars, germanBrands)
print(germanShowroom)

chinaShowroom = distributeCars(cars, chinaBrands)
print(chinaShowroom)