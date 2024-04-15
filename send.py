import csv
import os
import markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
from settings import SENDER_EMAIL, PASSWORD, DISPLAY_NAME

def get_msg(csv_file_path, template):
    with open(csv_file_path, 'r') as file:
        headers = file.readline().split(',')
        headers[len(headers) - 1] = headers[len(headers) - 1][:-1]
    with open(csv_file_path, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            required_string = template
            for header in headers:
                value = row[header]
                required_string = required_string.replace(f'${header}', value)
            yield row['EMAIL'], row['Ticket-ID'], required_string  # Return Ticket-ID as well

def confirm_attachments(ticket_id):
    file_name = f'{ticket_id}'  # Assuming the image file name is Ticket-ID.jpg
    file_path = os.path.join('QR Generated', file_name)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            content = f.read()
        return {'name': file_name, 'content': content}
    else:
        print(f"No image found for Ticket-ID: {ticket_id}")
        return None

def send_emails(server: SMTP, template):
    sent_count = 0

    for receiver, ticket_id, message in get_msg('data.csv', template):
        multipart_msg = MIMEMultipart("alternative")
        multipart_msg["Subject"] = message.splitlines()[0]
        multipart_msg["From"] = DISPLAY_NAME + f' <{SENDER_EMAIL}>'
        multipart_msg["To"] = receiver

        text = message
        html = markdown.markdown(text)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        multipart_msg.attach(part1)
        multipart_msg.attach(part2)

        attachment = confirm_attachments(ticket_id)
        if attachment:
            attach_part = MIMEImage(attachment['content'])
            attach_part.add_header('Content-Disposition', f"attachment; filename={attachment['name']}")
            multipart_msg.attach(attach_part)

        try:
            server.sendmail(SENDER_EMAIL, receiver, multipart_msg.as_string())
            sent_count += 1
        except Exception as err:
            print(f'Problem occurred while sending to {receiver}: {err}')

    print(f"Sent {sent_count} emails")

if __name__ == "__main__":
    host = "smtp.gmail.com"
    port = 587

    with open('compose.md') as f:
        template = f.read()

    server = SMTP(host=host, port=port)
    server.connect(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user=SENDER_EMAIL, password=PASSWORD)

    send_emails(server, template)

    server.quit()
