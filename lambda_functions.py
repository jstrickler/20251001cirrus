fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

print(sorted(fruits, key=lambda f: f[-1]))

x = lambda f: f[-1]
print(f"{x("pear") = }")

funcs = {
    'doit': lambda x: x * 10,
    'other': lambda x: x + 5,
}