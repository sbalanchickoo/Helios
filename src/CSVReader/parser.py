import csv, json

file_name = '.\\TestFiles\\Csv_Valid_2.CSV'
file_name1 = '.\\TestFiles\\Csv_Valid_1.CSV'

rows = []
jsonrows = []

with open(file_name, newline='') as csv_file:
    # reader = list(csv.DictReader(csv_file))
    reader = csv.DictReader(csv_file)
    for row in reader:
        if {'date', 'bankdescription', 'description', 'usercomments', 'amount', 'net', 'vat'} <= set(row):
            newrow = dict((k, row[k]) for k in ('date', 'bankdescription', 'description', 'usercomments', 'amount', 'net', 'vat'))
            if newrow not in rows:
                rows.append(newrow)

with open(file_name1, newline='') as csv_file:
    # reader = list(csv.DictReader(csv_file))
    reader = csv.DictReader(csv_file)
    for row in reader:
        if {'date', 'bankdescription', 'description', 'usercomments', 'amount', 'net', 'vat'} <= set(row):
            newrow = dict((k, row[k]) for k in ('date', 'bankdescription', 'description', 'usercomments', 'amount', 'net', 'vat'))
            if newrow not in rows:
                rows.append(newrow)

jsonrows = json.dumps(rows)

print(jsonrows)

for row in rows:
    print(row)
# with open(file_name1, newline='') as csv_file:
#     reader1 = list(csv.DictReader(csv_file))
#
#     for row in reader1:
#         if (row not in reader):
#             reader.append(row)
#
# # rows = json.dumps()
# for row in reader:
#     rows.append(json.dumps(row))
#
#
# for row in rows:
#     print(row[0])