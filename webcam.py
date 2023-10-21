

# def webcam():
#     import cv2
#     # define a video capture object
#     #
#     vid = cv2.VideoCapture(0)

#     while (True):
#         # Capture the video frame
#         #
#         ret, frame = vid.read()
#         # Display the resulting frame
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     # After the loop release the cap object
#     vid.release()
#     # Destroy all the windows
#     cv2.destroyAllWindows()


# webcam()

import cv2


def take_photo():
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
            cv2.imwrite('photo.jpg', frame)  # Save the frame as 'photo.jpg'
            print("Photo saved as 'photo.jpg'")
            break
        elif key == ord('q'):
            break

    # Release the video capture object and close the window
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    take_photo()
