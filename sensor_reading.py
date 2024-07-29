import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
SOUND_SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)

# Open the file in append mode
with open('sound_data.txt', 'a') as file:
    try:
        while True:
            # Read the digital signal from the sound sensor
            sound_detected = GPIO.input(SOUND_SENSOR_PIN)
            
            # Get the current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Write the data to the file
            file.write(f"Time: {timestamp}, Sound Detected: {sound_detected}\n")
            
            # Print the data to the console for debugging
            print(f"Time: {timestamp}, Sound Detected: {sound_detected}")
            
            # Wait for a short interval before the next reading
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Program terminated")
    finally:
        GPIO.cleanup()
