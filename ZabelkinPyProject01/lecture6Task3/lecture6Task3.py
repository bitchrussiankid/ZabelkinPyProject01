sales = {
    'Ivanov': {'mon': 120, 'tue': 135, 'wed': 140, 'thu': 130, 'fri': 125},
    'Petrov': {'mon': 90, 'tue': 110, 'wed': 95, 'thu': 105, 'fri': 115},
    'Sidorov': {'mon': 150, 'tue': 140, 'wed': 160, 'thu': 145, 'fri': 155}
}

employees = [
    "Ivanov",
    "Petrov",
    "Sidorov"
    ]

# Find average sales of each employee and the amount of sales per day:
averageSalesWeek = {}
salesPerDay = {}

for i in range(len(employees)):
    if employees[i] in sales.keys():
        averageSalesWeek[employees[i]] = sum(sales[employees[i]].values())
        for key, value in sales[employees[i]].items():
            if key in salesPerDay.keys():
                salesPerDay[key] += value
            else: 
                salesPerDay[key] = value

# Find agerage daily sales:
averageSalesDay = {}
for key, value in salesPerDay.items():
    averageSalesDay[key] = round((value / len(sales)), 1)

# Sales results:

print("Total sales managers:")
for key, value in averageSalesWeek.items():
    print(f"{key}: {value}")

print("\nAverage sales by day:")
for key, value in averageSalesDay.items():
    print(f"{key}: {value}")

# Who sold more?
for key, value in averageSalesWeek.items():
    if value == max(averageSalesWeek.values()):
        print(f"\n{key} sold the most this week: {value}$!")

# What day of the week is the most successful for sales?
for key, value in averageSalesDay.items():
    if value == max(averageSalesDay.values()):
        print(f"\n{key.capitalize()} - is the most successful day in terms of average sales: {value}$!")

