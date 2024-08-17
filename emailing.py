import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_SENDER = 'nandadattaburi2003@gmail.com'
PASSWORD = "hqhcphkkuhersvah"
RECEIVER = 'nandadattaburi2003@gmail.com'


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey we just saw a new customer!")

    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_SENDER, PASSWORD)
    gmail.sendmail(EMAIL_SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path='images/20.png')