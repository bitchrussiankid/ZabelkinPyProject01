countryCapitals = {
    "Germany": "Berlin",
    "Italy": "Rome",
    "France": "Paris",
    "Spain": "Madrid"   
    }

print(countryCapitals)

capDictKeys = list(countryCapitals.keys())
capDictValues = list(countryCapitals.values())
capDictItems = list(countryCapitals.items())

print(f"\n\n{capDictKeys}\n{capDictValues}\n{capDictItems}\n\n")


newCountryCapitals = {}
for i in range(len(countryCapitals)):
    newCountryCapitals[capDictKeys[i]] = capDictValues[i]

print(newCountryCapitals)