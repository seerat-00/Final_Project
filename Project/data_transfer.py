import os
import serial
import time
import firebase_admin
from firebase_admin import credentials, db
import adafruit_dht
import board

# JSON file path for Firebase credentials
json_path = "credentials.json"

# Firebase setup using JSON path
if os.path.exists(json_path):
    cred = credentials.Certificate(json_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://raspberry-camera-a4a87-default-rtdb.firebaseio.com/'  # Replace with your Firebase URL
    })
else:
    print("Error: Firebase JSON credential file not found.")
    exit(1)

# Serial communication setup for Arduino
serial_port = '/dev/ttyACM0'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

# DHT22 sensor setup on Raspberry Pi using 'board' for GPIO pin
DHT_SENSOR = adafruit_dht.DHT22(board.D4)  # Use the GPIO pin from 'board' library

# Function to read DHT22 data
def read_dht22():
    humidity, temperature = None, None
    max_retries = 5  # Number of retries
    for _ in range(max_retries):
        try:
            humidity = DHT_SENSOR.humidity
            temperature = DHT_SENSOR.temperature
            if humidity is not None and temperature is not None:
                break
        except RuntimeError as e:
            print(f"Error reading DHT22 sensor: {e}")
        time.sleep(2)  # Delay before retrying
    return humidity, temperature

print("Starting data collection and sending to Firebase...")

try:
    while True:
        # Read data from Arduino via serial port
        if ser.in_waiting > 0:
            arduino_data = ser.readline().decode('utf-8').strip()
            print("Arduino Data received:", arduino_data)

            # Read data from DHT22 sensor
            humidity, temperature = read_dht22()
            if humidity is not None and temperature is not None:
                print(f"DHT22 Data - Temperature: {temperature}C, Humidity: {humidity}%")
            else:
                print("Failed to retrieve data from DHT22 sensor")

            # Combine Arduino and DHT22 data and send to Firebase
            sensor_data = {
                'timestamp': time.time(),
                'arduino_data': arduino_data,
                'dht22_temperature': temperature,
                'dht22_humidity': humidity
            }

            # Send combined data to Firebase Realtime Database
            ref = db.reference('sensor_data')
            try:
                ref.push(sensor_data)
                print("Data sent to Firebase.")
            except Exception as e:
                print(f"Error sending data to Firebase: {e}")

        time.sleep(2)  # Delay between data readings

except KeyboardInterrupt:
    print("Data collection stopped.")
finally:
    ser.close()
    DHT_SENSOR.exit()  # Clean up GPIO resources
