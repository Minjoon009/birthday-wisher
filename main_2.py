import random
import pandas
import smtplib
import datetime as dt

MY_EMAIL = "aungheinhtetahhj2@gmail.com"
PASSWORD = "rtwr pngn hzoh npgw"
today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month,data_row.day): data_row for (index,data_row) in data.iterrows()}
def send_email(recipient_addr,message):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_addr,
            msg=f"Subject:Happy Birthday!\n\n{message}"
        )
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents =  contents.replace("[NAME]",birthday_person["name"])
    send_email(birthday_person["email"],contents)
