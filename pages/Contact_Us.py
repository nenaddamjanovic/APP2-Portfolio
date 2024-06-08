import streamlit as st

st.set_page_config(layout="wide")

st.header("Contact me")

with st.form(key="key_mail_form"):
    user_email = st.text_input(label="Put email address", key="key_email_input")
    message = st.text_area(label="Write your message", key="key_message")
    button = st.form_submit_button(label="Submit")
    if button:
        message = message + user_email
        print(button)
        print("i was pressed")