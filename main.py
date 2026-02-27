import smtplib
import pandas
import datetime as dt
import random
birthday_data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
now = dt.datetime.now()
now_month = now.month
now_day = now.day
def get_random_letter(name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        contents =  contents.replace("[NAME]",name)
    return contents
def send_email(recipient_addr,message):
    my_email = "aungheinhtetahhj2@gmail.com"
    password = "rtwr pngn hzoh npgw"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_addr,
            msg=f"Subject:Happy Birthday\n\n{message}"
        )
for data in birthday_data:
    if data["month"] == now_month and data["day"] == now_day:
        letter_content = get_random_letter(name="Aung Hein Htet")
        recipient_email = data["email"]
        send_email(recipient_addr=recipient_email,message=letter_content)





