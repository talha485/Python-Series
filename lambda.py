users = [
    {"name": "Ali", "age": 25},
    {"name": "Talha", "age": 22},
    {"name": "Ahmed", "age": 30}
]
sorted_users = sorted(users, key=lambda u:u['age'])
print(sorted_users)