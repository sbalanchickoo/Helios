import csv
import json

file_path = '.\\TestFiles\\'
file_name = file_path + 'Csv_Valid_2.CSV'
file_name1 = file_path + 'Csv_Valid_1.CSV'
fields = ['date', 'bankdescription', 'description', 'usercomments', 'amount', 'net', 'vat']
rows = []


def get_bank_metadata_from_file(file, fields_required=fields):
    file_rows = []
    try:
        with open(file, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for file_row in reader:
                if set(fields_required) <= set(file_row):
                    new_row = dict((k, file_row[k]) for k in fields_required)
                    file_rows.append(new_row)
    except FileExistsError:
        print(f"File [{file_path}] not found")
    except Exception as error:
        print(error)
    return file_rows


def consolidate_bank_metadata(bank_metadata_list):
    for list_row in bank_metadata_list:
        if list_row not in rows:
            rows.append(list_row)


consolidate_bank_metadata(get_bank_metadata_from_file(file_name1))
json_rows = json.dumps(rows)

print(json_rows)

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