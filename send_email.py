import smtplib
import ssl
import os


def send_email(message):
    """
    Funkcija prihvata message i izvršava slanje maila
    :param message:
    :return:
    """
    host = "smtp.gmail.com"
    port = 465
    username = "informaticarmreze@gmail.com"  # Naš email
    password = os.getenv("PASSWORD_GMAIL")  # password = "zytr epbx ofor chps"
    receiver = "informaticarmreze@gmail.com"  # Testiramo sa istim mailom, kome šaljemo

    sslcontext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=sslcontext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
