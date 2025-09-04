import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import pandas as pd
import os

# --- Configuration ---
SENDER_EMAIL = "vasanthitammana56@gmail.com"
SENDER_PASSWORD = "lwrj qnha aezp nrma"  # Gmail App Password

PARTICIPANTS_FILE_PATH = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/students.csv"
CERTIFICATES_DIR = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/generated_certificates"

def send_certificate_email(receiver_email, name, certificate_path):
    if not certificate_path or not os.path.exists(certificate_path):
        print(f"⚠ Certificate not found for {name}, skipping email.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = f"Certificate of Appreciation for {name}"

        body = (
            f"Hello {name},\n\n"
            "Congratulations on your participation in the hackathon!\n"
            "Please find your certificate of appreciation attached.\n\n"
            "Best regards,\n"
            "The Hackathon Team"
        )
        msg.attach(MIMEText(body, 'plain'))

        with open(certificate_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(certificate_path)}")
        msg.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
            print(f"📧 Successfully sent certificate to {receiver_email}")

    except Exception as e:
        print(f"❌ Error sending email to {receiver_email}: {e}")

def main():
    if not os.path.exists(PARTICIPANTS_FILE_PATH):
        print("❌ Participants file not found.")
        return

    df = pd.read_csv(PARTICIPANTS_FILE_PATH, encoding="latin1")

    for index, row in df.iterrows():
        name = row['Name']
        email = row['Email']
        certificate_path = os.path.join(CERTIFICATES_DIR, f"{name.replace(' ', '_')}_certificate.png")
        print(f"\n➡ Sending email to {name} ({email})")
        send_certificate_email(email, name, certificate_path)

if __name__ == "__main__":
    main()
