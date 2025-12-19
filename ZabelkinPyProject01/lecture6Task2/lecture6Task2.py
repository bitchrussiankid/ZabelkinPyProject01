words = ["apple", 
         "banana", 
         "apple", 
         "orange", 
         "banana", 
         "apple", 
         "pear", 
         "orange", 
         "banana", 
         "apple"
         ]

wordsAndCounts = {}
for i in range(len(words)):
    if words[i] in wordsAndCounts.keys():
        wordsAndCounts[words[i]] += 1
    else:
        wordsAndCounts[words[i]] = 1

print(wordsAndCounts)

for key, value in wordsAndCounts.items():
    if value == max(wordsAndCounts.values()):
        print(f"The word {key} was found more often than others: {value} times\n")
        
    if value > 2:
        print(f"The word {key} was found more than 2 times\n")