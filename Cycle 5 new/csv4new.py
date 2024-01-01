import csv

with open('studentdetails.csv', 'r') as csv_f:
    csv_r = csv.DictReader(csv_f)
    
    print("Roll No   Student Name")
    print("----------------------")
    
    for line in csv_r:
        print(f"{line['Roll No']:8} {line['Student Name']}")
