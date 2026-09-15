# Student Camera Attention Detector

A script that uses face detection to monitor whether a student stays visible in front of the camera during an online session.
It displays a live camera feed with the number of detected faces, and prints a warning if no face is detected for more than 5 minutes in a row.

## Requirements
- Python 3.11 or higher
- A working webcam

## Setup

1. Clone this repository
2. Install the required libraries:

pip install -r requirements.txt

## Usage

Run the script:
python Student_detection.py


A window will open showing the camera feed with a red rectangle drawn around any detected face(s), along with a live count in the top-left corner. To stop the program, press `q` while the camera window is focused, or press Ctrl+C in the terminal.

## How it works

- Face detection is done using OpenCV's built-in Haar Cascade classifier, which looks for face-like patterns in each frame.
- The script tracks how long a face has been absent from the frame. If more than 5 minutes pass with no face detected, it prints a one-time warning to the terminal.
- The warning resets once a face is detected again, so it can trigger again if the student steps away a second time.

## Notes
- This uses basic face detection, not face recognition — it does not identify who the person is, only whether a face is present.
- Detection accuracy can drop with poor lighting, side angles, or partial face coverage.
