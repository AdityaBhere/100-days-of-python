import os
from dotenv import load_dotenv
import smtplib
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email = os.environ["MY_EMAIL"]
        self.my_email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.smtp_address = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])

    def send_email(self, email_list, email_body):
        with smtplib.SMTP(host=str(self.smtp_address), port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8'))

