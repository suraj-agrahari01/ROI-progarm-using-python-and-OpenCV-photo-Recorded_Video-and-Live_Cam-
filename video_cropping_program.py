import cv2

# Open the video file
video_path = 'darshan.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get the width and height of the video frames
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the region to crop (left, top, width, height)
crop_x = 83
crop_y = 316
crop_width = 214
crop_height = 296

# Create an output video file
output_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 30.0, (crop_width, crop_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Crop the frame
    cropped_frame = frame[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]

    # Write the cropped frame to the output video
    out.write(cropped_frame)

    # Display the cropped frame (optional)
    cv2.imshow('Cropped Video', cropped_frame)
    cv2.imshow('original Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video objects
cap.release()
out.release()
cv2.destroyAllWindows()

# import cv2

# # Open the video file
# video_path = 'darshan.mp4'
# cap = cv2.VideoCapture(video_path)

# # Check if the video file was opened successfully
# if not cap.isOpened():
#     print("Error: Could not open video file.")
#     exit()

# # Initialize a counter to keep track of the frame number
# frame_number = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break  # End of video

#     frame_number += 1

#     # Check if this is the fifth frame
#     if frame_number == 30:
#         # Select ROI in the fifth frame
#         roi = cv2.selectROI(frame)

#         # Extract the coordinates of the selected bounding box
#         x, y, w, h = roi

#         print(
#             f"Selected Bounding Box in Fifth Frame: x={x}, y={y}, width={w}, height={h}")

#         # You can break out of the loop once you've obtained the ROI from the fifth frame
#         break

# # Release video objects
# cap.release()
# cv2.destroyAllWindows()
