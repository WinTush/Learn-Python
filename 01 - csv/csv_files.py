import csv


employees = [
    ["Sabrina Dobrev", "808-6281-2792", "IT Specialist"],
    ["Corey Marshall", "382-3728-7836", "Manager"],
    ["Larry Mathiu", "536-7269-3572", "Cashier"]
]

with open("csv_file.txt", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)

with open("csv_file.txt") as file:
    csv_f = csv.reader(file)
    for name, phone, role in csv_f:
        print(f"Name: {name}, Phone: {phone}, Role: {role}")
