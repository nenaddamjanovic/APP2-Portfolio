import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
username = "informaticarmreze@gmail.com"  # Naš email
password = "zytr epbx ofor chps"  # Šifra sa gmail podešavanja za APP
receiver = "informaticarmreze@gmail.com"  # Testiramo sa istim mailom, kome šaljemo

context = ssl.create_default_context()

message = """\
Subject: Test python message
Hi! How are you, Bye"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)