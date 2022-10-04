import csv

# CSV WITHOUT HEADER
# with open("data/addresses.csv") as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     # print(list(reader))
#     for row in reader: # row is a list
#         print(row[0])

# CSV WITH HEADER
with open("data/biostats.csv") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader))
    for row in reader: #row a dict
        print(row["Name"])