import openpyxl
import mysql.connector

# Load the Excel workbook
workbook = openpyxl.load_workbook('pythonexcel.xlsx')

# Select the worksheet you want to read from
worksheet = workbook['Sheet1']

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondb"
)

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Loop through the rows and columns in the worksheet
for row in worksheet.iter_rows(min_row=2):
    # Extract the data from each cell in the row
    name = row[0].value
    age = row[1].value
    city = row[2].value

    # Insert the data into the MySQL database
    query = "INSERT INTO mytable (name, age, city) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, city))
    db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
