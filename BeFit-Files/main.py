import numpy as np
import cv2


main_vid = cv2.VideoCapture('BeFit-Files/mainVideo.mp4')
sign_lang = cv2.VideoCapture('BeFit-Files/interpreter.mp4')

while main_vid.isOpened() and sign_lang.isOpened():
    ret_main, frame_main = main_vid.read()
    ret_interpreter, frame_interpreter = sign_lang.read()

    if not ret_main or not ret_interpreter:
        break

    # Assume both videos have the same frame rate and length
    # If not, you'll need to handle frame rate conversion and synchronization
        # Resize interpreter frame to fit PiP window
    interpreter_small = cv2.resize(frame_interpreter, (width, height))

    # Define position for PiP (e.g., bottom right corner)
    x_offset = main_frame_width - width - 10
    y_offset = main_frame_height - height - 10

    # Overlay interpreter video onto main video
    frame_main[y_offset:y_offset+height, x_offset:x_offset+width] = interpreter_small

    # Display the result (for testing)
    cv2.imshow('PiP Video', frame_main)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (main_frame_width, main_frame_height))

while main_video.isOpened() and sign_lang.isOpened():
    ret_main, frame_main = main_vid.read()
    ret_interpreter, frame_interpreter = sign_lang.read()

    if not ret_main or not ret_interpreter:
        break

    # Resize interpreter frame to fit PiP window
    interpreter_small = cv2.resize(frame_interpreter, (width, height))

    # Define position for PiP (e.g., bottom right corner)
    x_offset = main_frame_width - width - 10
    y_offset = main_frame_height - height - 10

    # Overlay interpreter video onto main video
    frame_main[y_offset:y_offset+height, x_offset:x_offset+width] = interpreter_small

    # Write the frame to the output file
    out.write(frame_main)

# Release everything
main_vid.release()
sign_lang.release()
out.release()
cv2.destroyAllWindows()
