# Email Sending Script

This Python script is designed to send emails with attachments to a list of recipients. It is particularly useful for sending emails with custom content and attachments, such as tickets or images.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (install using `pip install`):
  - `smtplib`
  - `email`
  - `tqdm`

## Getting Started

1. Clone this repository to your local machine or download the script files.

2. Prepare your email content:
   - Create a `data.csv` file with a list of recipients' information. It should have two columns: `Image_ID` and `Email`.
   - Create a `content.txt` file with the common email content that you want to send to all recipients.
   - Create a `subjects.txt` file with custom email subjects for each recipient, one subject per line.

3. Create an `Images` folder and place your ticket images inside it. Make sure the image filenames correspond to the `Image_ID` values in your `data.csv` file.

4. Optionally, create a `credentials.txt` file with your Gmail credentials in the following format:

email_sender = "your_email@gmail.com"
email_password = "your_password"


**Note:** Make sure to enable "less secure apps" in your Gmail settings if you use your Gmail account for sending emails.

## Usage

1. Open a terminal/command prompt and navigate to the directory containing the script files.

2. Run the script using the following command:

```bash
python email_sender.py

The script will start sending emails to the recipients in your data.csv file using the provided content and attachments.

Customization
You can customize the email subject and content by modifying the subjects.txt and content.txt files.
Ensure that the image filenames in the Images folder match the Image_ID values in your data.csv file.
Troubleshooting
If you encounter issues with sending emails, check the following:
Ensure that you have a working internet connection.
Verify that your Gmail credentials in credentials.txt are correct.
Check that the image filenames in the Images folder match the Image_ID values in data.csv.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This script was created for educational and demonstrative purposes.
Credits to the Python community and libraries used in this project.
