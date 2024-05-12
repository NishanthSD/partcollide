import json
import cv2
import numpy as np

# Read JSON file
with open("TEST.json", "r") as file:
    data = json.load(file)

# Get the number of particles
num_particles = len(data)

# Define video parameters
fps = 30
width, height = 300, 300  # Dimensions of the container
duration = max(len(path) for path in data.values()) // fps

# Create video writer
video_writer = cv2.VideoWriter("simulatiwon.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

# Iterate through each time step
for step in range(duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)  # Black background

    # Draw particles
    for particle_id, particle_path in data.items():
        if step < len(particle_path):
            x, y = map(int, particle_path[step])
            cv2.circle(frame, (x, y), 2, (255, 255, 255), -1)  # Draw white particle

    # Write frame to video
    video_writer.write(frame)

# Release video writer
video_writer.release()

print("Video saved as simulation.mp4")
