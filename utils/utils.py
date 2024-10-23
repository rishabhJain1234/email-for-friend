import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import streamlit as st
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()
import os


def generate_email(company_name, person_name, mail_type):
    if mail_type=='new-company':
        return f'''Dear {person_name},

I hope you are doing well.

My name is Priya Rajput, Interning as an Investment analyst representing Xpertiz, a distinguished Investment Banking firm based in Bangalore, India. We specialize in providing comprehensive M&A, Funding, Transformation, and Turnaround services to a wide range of Indian and Global companies.

I am writing to you today because we have been closely monitoring the growth of {company_name} with great interest. We believe that {company_name} has a strong foundation and a bright future.

At Xpertiz, we see a significant opportunity to partner with our clients to fuel the expansion strategies. We are keenly interested in exploring a strategic investment through our client interested in your company.  In fact, with our extensive experience and successful track record, we can be a valuable asset to your team.

Xpertiz recently closed a major deal and also working on few other deals with Infosys, further solidifying our expertise in the IT and consulting sector. We have a strong client base of established companies like Accenture, Capgemini, L&T Mindtree, HeroElectronix, and many more. Currently, we're facilitating deals worth $1.5 billion across various sectors, including semiconductor services, IT services, digital transformation, cybersecurity, enterprise applications, fintech, and more.

We're confident that our experience and network can greatly benefit {company_name}. I've attached our company profile for you to look over.

I'd be happy to schedule a call or meeting to discuss a potential collaboration and explore how Xpertiz can help you achieve your growth objectives. Please let me know when you're available.

Looking forward to your response. Please connect us with your M&A or strategic investment team to get to know your broad M&A category to explore other potential opportunities.

Thank you for your time and consideration.

Best Regards
Priya Rajput
3rd floor, Awfis, Tower B, Prestige Shantiniketan Commercial, Whitefield, Bangalore-560066'''
    else:
        return f'''Hi {person_name},

I hope you are doing well.
I just wanted to follow up with you on an email I sent earlier to see if you had a chance to review the opportunity that we shared with you. I understand that you must have a busy schedule.
I want to reiterate that we are very interested in collaborating with you and your team, and if you have any questions or concerns, please do not hesitate to reach out. 
I would be happy to schedule a call to discuss the opportunity and give you more details about the company we are working with.
Looking forward to your response. Please connect us with your M&A or strategic investment team to get to know your broad M&A category to explore other potential opportunities.
Thank you for your time and consideration. I look forward to hearing from you soon.

Best Regards,
Priya Rajput 
3rd floor, Awfis, Tower B, Prestige Shantiniketan Commercial, Whitefield, Bangalore-560066
    '''
def send_email(email_id, actual_email, subject):
            sender_email = st.secrets["EMAIL"]
            sender_password = st.secrets["PASSWORD"]
            
            # sender_email = os.getenv("EMAIL")
            # sender_password = os.getenv("PASSWORD")

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email_id
            msg['Subject'] = subject

            msg.attach(MIMEText(actual_email, 'plain'))
            
            # #attach image here
            # image_path = "image.png"
            # with open(image_path, "rb") as image_file:
            #     image = MIMEBase("application", "octet-stream")
            #     image.set_payload(image_file.read())
            #     encoders.encode_base64(image)
            #     image.add_header(
            #         "Content-Disposition",
            #         f"attachment; filename={os.path.basename(image_path)}",
            #     )
            #     msg.attach(image)
            with open("Xpertiz Company Profile Sep 2024.pdf", "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename=Xpertiz Company Profile Sep 2024",
                )
                msg.attach(part)

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, email_id, text)
                server.quit()
                print('Email sent successfully!')
                st.success("Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {e}")
                st.error(f"Failed to send email: {e}")