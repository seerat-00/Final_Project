import time
from picamera2 import Picamera2
from datetime import datetime

# Initialize the camera
picam2 = Picamera2()

# Start the camera
picam2.start()

try:
    while True:
        # Get the current time for naming the image file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"image_{timestamp}.jpg"
        
        # Capture and save the image
        picam2.capture_file(filename)
        print(f"Captured image: {filename}")
        
        # Wait for 2 minutes (120 seconds) before capturing the next image
        time.sleep(120)

except KeyboardInterrupt:
    # Stop the camera when exiting the program
    print("Program interrupted. Stopping the camera.")
    picam2.stop()
