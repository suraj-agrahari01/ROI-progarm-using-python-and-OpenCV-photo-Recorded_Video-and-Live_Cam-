import cv2


def crop_video_with_roi(output_path):
    def crop_frame(frame, x, y, width, height):
        return frame[y:y+height, x:x+width]

    # Initialize the video capture object
    vid = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    if not vid.isOpened():
        print("Error: Could not open webcam.")
        return

    crop_x = None
    crop_y = None
    crop_width = None
    crop_height = None

    recording = False
    frame_number = 0
    out = None  # Initialize the out object

    while True:
        ret, frame = vid.read()
        if not ret:
            break

        frame_number += 1

        if crop_x is not None and crop_y is not None and crop_width is not None and crop_height is not None:
            cropped_frame = crop_frame(
                frame, crop_x, crop_y, crop_width, crop_height)
            cv2.imshow('Cropped Video', cropped_frame)

            if recording:
                out.write(cropped_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('s'):
            if recording:
                print("Stopped recording.")
                out.release()  # Release the video writer
                recording = False
            else:
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(
                    output_path, fourcc, 30.0, (crop_width, crop_height))
                print("Started recording.")
                recording = True
        elif key == ord('r'):
            crop_x = None
            crop_y = None
            crop_width = None
            crop_height = None

        if crop_x is None or crop_y is None or crop_width is None or crop_height is None:
            if frame_number == 40:  # Select ROI in the 40th frame
                # Select ROI by dragging a rectangle
                roi = cv2.selectROI(frame)
                x, y, w, h = roi

                print(
                    f"Selected Bounding Box: x={x}, y={y}, width={w}, height={h}")

                crop_x = x
                crop_y = y
                crop_width = w
                crop_height = h

    vid.release()
    cv2.destroyAllWindows()

    return


if __name__ == "__main__":
    output_video_path = 'final_output.mp4'
    crop_video_with_roi(output_video_path)
