from pprint import pprint
c = 0
if c : 
    print("c is not zero")
if c == 0 : 
    print("c is zero")
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28}
]
for user in users:
    pprint(user)

d ={
    "first": 1,
    "second": 2,
    "third": 3
}

for key in d: 
    pprint(key)
for value in d.values(): 
    pprint(value)
for key, value in d.items(): 
    pprint((key, value))

for i in range(5):
    for j in range(5):
        print (i, j) 