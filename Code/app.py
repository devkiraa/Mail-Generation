import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
from tqdm import tqdm

# Function to send an email with the ticket attached
def send_ticket_email(sender_email, sender_password, receiver_email, ticket_path, image_id, email_subject, email_content):
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email_subject  # Use custom subject

    # Create an HTML version of the email content
    email_html = f"""\
    <html>
      <body>
        {email_content}
      </body>
    </html>
    """

    # Attach the HTML content
    message.attach(MIMEText(email_html, "html"))

    # Attach the ticket image to the email
    with open(ticket_path, "rb") as ticket_file:
        img = MIMEImage(ticket_file.read())
    message.attach(img)

    # Connect to the SMTP server (for Gmail)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Close the server connection
    server.quit()

# Function to validate email addresses using regular expressions
def is_valid_email(email):
    # Regular expression to validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    # Your Gmail credentials (make sure to enable less secure apps in your Gmail settings)
    email_sender = ""
    email_password = ""

    # Read data from the data.csv file
    with open("Script/data.csv", "r") as csv_file:
        lines = csv_file.readlines()[1:]  # Skip the header line
        invalid_emails = []

        # Count the number of emails to send
        num_emails_to_send = len(lines)

        # Read custom email subjects from a file
        with open("Script/subjects.txt", "r") as email_subjects_file:
            email_subjects = email_subjects_file.read().splitlines()

        # Read common email content from a file
        with open("Script/content.txt", "r") as common_content_file:
            common_content = common_content_file.read()

        with tqdm(total=num_emails_to_send, desc="Sending Emails") as main_pbar:
            for i, line in enumerate(lines):
                data = line.strip().split(",")
                image_id = data[0].strip()  # Assuming Image_ID is in the first column
                receiver_email = data[1].strip()  # Assuming email is in the second column

                if not is_valid_email(receiver_email):
                    print(f"Invalid email: {receiver_email} for Image ID {image_id}")
                    invalid_emails.append((image_id, receiver_email))
                else:
                    # Construct the image filename based on Image_ID
                    image_name = f"{image_id}.jpg"
                    ticket_path = os.path.join("Script/Images", image_name)

                    if os.path.exists(ticket_path):
                        print(f"Sending email to: {receiver_email} for Image ID {image_id}")

                        # Use common subject and content for all emails
                        send_ticket_email(
                            email_sender, email_password, receiver_email, ticket_path, image_id,
                            email_subjects[i], common_content  # Use common subject and content
                        )

                        print(f"Email sent successfully to: {receiver_email} for Image ID {image_id}")
                    else:
                        print(f"Image not found for Image ID {image_id}")

                main_pbar.update(1)

        if invalid_emails:
            print("\nInvalid emails:")
            for image_id, invalid_email in invalid_emails:
                print(f"Image ID {image_id}: {invalid_email}")

        # Calculate the number of emails sent
        num_emails_sent = num_emails_to_send - len(invalid_emails)
        print(f"Total emails sent: {num_emails_sent}")
        print(f"Total emails not sent due to invalid addresses: {len(invalid_emails)}")

if __name__ == "__main__":
    main()
