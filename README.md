# Motion Detection and Email Notification

This project detects motion in video frames captured from a webcam and sends an email notification when motion is detected with images attached. This project uses the OpenCV library for image processing and object detection.

## Dependencies

- Python 3.x
- OpenCV (cv2)
- smtplib
- ssl
- email.message
- imghdr

## Installation

1. Clone the repository:

   ```bash
        git clone https://github.com/your-username/your-repo.git

2. Change into the project directory:


      cd your-repo


3. Install the required dependencies:


      pip install -r requirements.txt


4. Usage


      Run the main.py script: python main.py


5. The script will start capturing video from the webcam.


      When motion is detected, an email notification will be sent to the specified email address, along with images as an attachment.

      Press 'q' to stop the script and exit.


   6. Configuration


    To configure the email settings, open the emailing.py script and modify the following variables:

    - SENDER: Sender's email address
    - PASSWORD: Sender's email password
    - RECEIVER: Receiver's email address