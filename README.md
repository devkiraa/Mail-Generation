# DevMail

This program is here to help to sent bulk amount of emails directly

## Features

- Send dynamic emails with unlimited variables pulling data from a CSV file.
- Supports Markdown Formatting & embed links or images.
- Supports Attaching any kind of files.

## Usage

1. Make sure you have Python installed on your system.
2. Download or clone the repo and then move into the automailer directory.
3. Install all dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. **Write your email inside `compose.md`** (supports markdown formatting)

    You can use variables, prefix them with $ sign.
    ```markdown
    Hi $NAME, your mail id is $EMAIL
    ```

6. **Prepare your data in `data.csv` file**. The first line (headers) must contain 'EMAIL' (uppercase) parameter.

7. **Attachments (Optional)**: If you want to include attachments, place them in the `ATTACH` directory.

8. **Set Up Credentials**: Create a file named `.env` and include the following credentials:

    ```plaintext
    display_name=Spiderman
    sender_email=your@example.com
    password=12345
    ```

    Replace the placeholder values with your real credentials. Note: Avoid using your original email password. Create a Gmail Account then turn on 2-step Verification, and then set up an App Password for automailer.

9. All set up 👍 you are now READY TO GO. **Run the `send.py` file**:

    ```bash
    python send.py
    ```

    You will be asked to confirm the attachments in the `ATTACH` folder. Upon confirmation, the application will start sending emails. You will receive a full success report after emails are sent.

## Getting Help

Please report an issue or ask your question in the issues section of the repository.

**Note**: This program focuses on simplicity and functionality. For advanced features or customizations, consider exploring additional functionalities or contributing to the project.
