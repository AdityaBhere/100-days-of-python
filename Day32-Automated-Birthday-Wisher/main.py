import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
today_weekday = now.weekday()

if today_weekday == 4:
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes)
        subject = quote.split('- ')[1].strip()
        text = quote.split('- ')[0]

        my_email = #your email
        password = #your app password

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= #recievers email,
                msg=f"Subject:{subject}\n\n{text}")
            connection.close()
