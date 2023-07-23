import csv
import json

def extract_data(file_name):
  data = []
  with open(file_name, 'r') as file:  
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        data.append({
            'PassengerId': row[0],
            'Age': row[1],
            'Fare': row[2]  # Fixed the column index for Fare
        })
  return data

def save_to_json(data, json_file_name):
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file)

data = extract_data('titanic.csv')
save_to_json(data, 'titanic_data.json')
