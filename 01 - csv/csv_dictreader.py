import csv


users = [
    {'name': 'Sol Mansi', 'username': 'solm', 'department': 'IT infrastructure'},
    {'name': 'Lio Nelson', 'username': 'lion', 'department': 'User Experience Research'},
    {'name': 'Charlie Grey', 'username': 'greyc', 'department': 'Development'},
]

keys = ['name', 'username', 'department']
with open('csv_dict.txt', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

with open('csv_dict.txt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'Name: {row["name"]}, Username: {row["username"]}, Department: {row["department"]}')
