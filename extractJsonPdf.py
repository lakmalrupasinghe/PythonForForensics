import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Titanic Data Extract', 0, 1, 'C')

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

def save_to_pdf(data, pdf_file_name):
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size = 12)

    line_height = 10
    for i, item in enumerate(data):
        pdf.cell(200, 10, txt = f"PassengerId: {item['PassengerId']}, Age: {item['Age']}, Fare: {item['Fare']}",ln = True)
    pdf.output(pdf_file_name)

data = extract_data('titanic.csv')
save_to_pdf(data, 'titanic_data.pdf')
