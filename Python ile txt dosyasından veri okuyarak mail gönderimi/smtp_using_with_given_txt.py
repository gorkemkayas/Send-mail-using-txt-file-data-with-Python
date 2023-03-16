import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(sender, receiver, subject):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    message_to_be_sent = """

    K A Y A   B A N K 

    You have to pay off your credit card debt
    We look forward to seeing you at our branch as soon as possible.

                                            Bank Manager: Gorkem KAYA

    """

    message_last_form = MIMEText(message_to_be_sent, "plain")
    message.attach(message_last_form)

    try:
        mail_server = smtplib.SMTP("smtp.gmail.com", 587)
        mail_server.ehlo()
        mail_server.starttls()

        mail_server.login("your mail", "your password")
        mail_server.sendmail(message["From"], message["To"], message.as_string())

        print("SMTP mail system worked successfully!\n\n")



    except:
        sys.stderr.write("There is an unknown problem!\n")
        sys.stderr.flush()


with open("odevtxtsi.txt","r",encoding="utf-8") as file1:
    for i in file1:
        i = i.split(",")
        print("isim: ",i[0])
        print("Mail: ",i[1])
        send_mail(i[0], i[1], "Credit Payment")










