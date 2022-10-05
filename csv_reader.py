import csv

# CSV WITHOUT HEADER
# with open('data/addresses.csv') as csv_file:
#     reader = csv.reader(csv_file, skipinitialspace=True)
#     # print(list(reader))
#     for row in reader:
#         print(f'name: {row[0]} - address: {row[2]}')

# CSV WITH HEADER
with open('data/biostats.csv') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)
    # print(list(reader))
    for row in reader:
        print(f'name: {row["Name"]} - age: {row["Age"]}')