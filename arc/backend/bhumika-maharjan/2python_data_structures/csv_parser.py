import csv

def csv_to_dicts(file_path):
    result = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(type(reader))
        for row in reader:
            result.append(dict(row))
    return result

data = csv_to_dicts('SCB_daily.csv')
print(data)

  