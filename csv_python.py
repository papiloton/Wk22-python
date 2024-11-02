import csv

with open("test.csv", 'w') as f:
    writer = csv.writer(f)
    HEADER=['Name', 'Cell', 'Profession', 'Email']
    writer.writerow(HEADER)
    writer.writerow(['Sammy', '555 555 5555', 'DevOps Engineer', 'kabodo@gmail.com'])