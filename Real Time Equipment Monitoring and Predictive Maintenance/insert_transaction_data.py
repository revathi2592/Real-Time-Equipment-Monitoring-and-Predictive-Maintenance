import csv
import psycopg2
from psycopg2 import sql
 
# Function to insert JSON data into PostgreSQL
def insert_json_data(file_path, db_params):
    # Read JSON data from file
    with open(file_path, 'r') as file:
        data = csv.reader(file)
        header = next(data)
   
    # Connect to PostgreSQL
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
   
    # Insert JSON data\
        for transaction in data:
            sensor_id = transaction[0]              # Column 0: SensorID
            device_id = transaction[1]              # Column 1: DeviceID
            ReadingTimestamp = transaction[2]               # Column 2: Timestamp
            temperature = float(transaction[3])      # Column 3: Temperature
            vibration_level = float(transaction[4])   # Column 4: VibrationLevel
            operating_hours = int(transaction[5])     # Column 5: OperatingHours
            status = transaction[6]
           
            cur.execute(
            sql.SQL("INSERT INTO EquipmentSensors (SensorID, DeviceID, ReadingTimestamp, Temperature, VibrationLevel, OperatingHours, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
            (sensor_id, device_id, ReadingTimestamp, temperature, vibration_level, operating_hours, status)
        )
           
   
            print(transaction)
    # Commit and close
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully")
 
# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'fabricadmin',
    'password': '<password>',
    'host': '<server-name>',
    'port': '5432'
}
 
# Path to your JSON file
file_path = 'Azure Database for PostgreSQL Integration\EquipmentSensorsData.csv'
 
# Insert data
insert_json_data(file_path, db_params)