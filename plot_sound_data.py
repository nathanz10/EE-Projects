import matplotlib.pyplot as plt
import datetime

# Initialize lists to store timestamps and sound detections
timestamps = []
sound_detections = []

# Open the file and read the data
with open('sound_data.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        if len(parts) == 2:
            timestamp_str = parts[0].replace('Time: ', '')
            sound_detected_str = parts[1].replace('Sound Detected: ', '')
            
            try:
                # Convert timestamp string to datetime object
                timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                sound_detected = int(sound_detected_str)
                
                # Append to lists
                timestamps.append(timestamp)
                sound_detections.append(sound_detected)
            except ValueError as e:
                print(f"Error parsing line: {line}, error: {e}")

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(timestamps, sound_detections, label='Sound Detected', marker='o')

# Formatting the graph
plt.xlabel('Time')
plt.ylabel('Sound Detected')
plt.title('Sound Detection Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
