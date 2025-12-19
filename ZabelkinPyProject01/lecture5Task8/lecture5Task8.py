import copy

dict1 = {
    "a": 1,
    "b": 2,
    "e": 5
    }

dict2 = {
    "c": 3,
    "d": 4,
    "e": 6     
    }

dict1.update(dict2)
dict3 = copy.deepcopy(dict1)
dict1.clear()
print(dict1)
print(dict2)
print(dict3)