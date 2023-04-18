import mysql.connector
from openpyxl import Workbook

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondb"
)

sql = "SELECT * FROM mytable WHERE age > 30"
cursor = db.cursor()
cursor.execute(sql)
results = cursor.fetchall()

# Create a new Excel workbook and sheet
wb = Workbook()
sheet = wb.active

# Write the results to the sheet
sheet.append(["Name", "Age", "City"])
for row in results:
    sheet.append(row)

# Save the workbook to a new Excel file
wb.save("output.xlsx")

# Close the database connection
cursor.close()
db.close()