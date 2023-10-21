import cv2


def take_photo_with_roi():
    # Initialize the video capture object
    vid = cv2.VideoCapture(0)

    while True:
        # Capture a single frame
        ret, frame = vid.read()

        # Display the frame
        cv2.imshow('Press "Space" to Take Photo', frame)

        # Check for key presses
        key = cv2.waitKey(1)

        # Press 'Space' to take a photo
        if key == ord(' '):
            roi = cv2.selectROI(frame)  # Select ROI by dragging a rectangle
            x, y, w, h = roi
            # Draw a green rectangle around the ROI
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('Selected ROI', frame)  # Show the selected ROI

            # Print bounding box coordinates
            print(
                f"Bounding Box Coordinates: x={x}, y={y}, width={w}, height={h}")

            cv2.imwrite('photo.jpg', frame)  # Save the frame as 'photo.jpg'
            print("Photo saved as 'photo.jpg'")
            break
        elif key == ord('q'):
            break

    # Release the video capture object and close the window
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    take_photo_with_roi()
