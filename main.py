import streamlit as st
from utils.utils import send_email, generate_email
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize session state variables
    if 'editable_email' not in st.session_state:
        st.session_state.editable_email = ''
    
    st.title("Priya's Email Sender")

    email_id = st.text_input("Enter Email ID to send email to")
    company_name = st.text_input("Enter Company Name")
    person_name = st.text_input("Enter Person Name")
    mail_type = st.selectbox("Select Mail Type", ["new-company", "follow-up"])
    
    if st.button("Submit"):
        generated_email = generate_email(company_name, person_name, mail_type)
        st.session_state.editable_email = generated_email  # Store the generated email in session state
    
    st.subheader("Generated Email")
    # Use the session state for editable email content
    editable_email = st.text_area("Generated Email Content", st.session_state.editable_email, height=300)

    st.subheader("Subject")
    # Use the session state for subject content
    subject = st.text_input("Subject", f'Investment Opportunity for {company_name} - Collaboration with Xpertiz')

    if st.button("Send Email"):
        send_email(email_id, editable_email, subject)
        st.balloons()

if __name__ == "__main__":
    main()
