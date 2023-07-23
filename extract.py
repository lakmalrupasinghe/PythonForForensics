import csv

def extract_data(file_name):
  with open(file_name, 'r') as file:  
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f'Passengerid:{row[0]}, Age: {row[1]}, Fare: {row[0]}')


extract_data('titanic.csv')

