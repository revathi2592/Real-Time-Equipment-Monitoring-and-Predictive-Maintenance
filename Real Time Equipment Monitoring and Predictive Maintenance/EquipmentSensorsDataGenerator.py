import uuid
import random
import pandas as pd
from datetime import datetime
 
# Constants
DEVICE_IDS = ['sen_010', 'sen_011', 'sen_012', 'sen_013', 'sen_014']  # Example device IDs
STATUS_CHOICES = ['Normal']
 
# Helper function to determine the status based on temperature and vibration level
def determine_status(temperature, vibration_level):
    if temperature > 80 or vibration_level > 8:
        return 'Fault'
    elif temperature > 60 or vibration_level > 5:
        return 'Warning'
    else:
        return 'Normal'
 
# Generate synthetic data for each device at the current timestamp
data = []
current_timestamp = datetime.now()  # Set current timestamp
 
for device_id in DEVICE_IDS:
    sensor_id = uuid.uuid4()  # Generate unique UUID for SensorID
    temperature = round(random.uniform(20.0, 80.0), 2)  # Temperature in range [20.0, 100.0]
    vibration_level = round(random.uniform(0.5, 7.0), 2)  # Vibration level in range [0.5, 10.0]
    operating_hours = random.randint(0, 500)  # Operating hours in range [0, 500]
    status = determine_status(temperature, vibration_level)  # Determine status
 
    # Add the record to data
    data.append([sensor_id, device_id, current_timestamp, temperature, vibration_level, operating_hours, status])
 
# Convert to a DataFrame for easy handling and display
df = pd.DataFrame(data, columns=['SensorID', 'DeviceID', 'Timestamp', 'Temperature', 'VibrationLevel', 'OperatingHours', 'Status'])
 
# Display the first few rows of the generated dataset
print(df.head())
 
# Save to a CSV file if needed
df.to_csv("/Azure Database for PostgreSQL Integration/EquipmentSensorsData.csv", index=False)
 
 