import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact me")

with st.form(key="key_mail_form"):
    user_email = st.text_input(label="Put email address", key="key_email_input")
    raw_message = st.text_area(label="Write your message", key="key_raw_message")

# Poruka se pravi sa tačno ovom formom i svim enterima.
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""  # Poruka se pravi sa tačno ovom formom i svim enterima.

    button = st.form_submit_button(label="Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

