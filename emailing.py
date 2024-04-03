import smtplib
from email.message import EmailMessage
import imghdr

host = "smtp.gmail.com"
port = 465
SENDER = "hredi1994@gmail.com"
PASSWORD = "mmrjrbvbhsbvhefo"
RECEIVER = "hredi1994@gmail.com"

def send_email(image):

    email_message = EmailMessage()
    email_message["Subject"] = "A new customer showed up"
    email_message.set_content("Hey, we just saw a new customer")

    with open(image, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP_SSL(host, port)
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image="images/10.png")