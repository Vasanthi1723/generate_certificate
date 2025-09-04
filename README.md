🎓 Certificate Generator :-
This is a Python project to automatically generate certificates for students/participants using data from a CSV file.
The script dynamically fills participant details (such as Name, Roll Number, Branch, Hackathon/Event Name, Topic, and Date) into a certificate template and adds the Principal’s signature in a signature-style font.

📂 Project Structure :-
certificate-generator/
│── certificate.py             # Main script to generate certificates
│── send_emails.py             # Script to send generated certificates via email
│── signature_font.ttf          # Signature font (e.g., GreatVibes)
│── template.png                # Certificate template image
│── students.csv                # CSV file with participant data
│── generated_certificates/     # Generated certificates saved here
│── README.md                   # Project documentation

✨ Features :-
📑 Dynamic Certificate Content – Automatically inserts student details into the certificate.
🖋️ Signature Font Support – Adds the Principal’s name in a signature-style font.
🖼️ Template Based – Works with any background certificate template (template.png).
🔄 Batch Generation – Reads all student details from students.csv and generates certificates in one go.
💾 Organized Output – Certificates are saved in the generated_certificates/ folder.

⚙️ Requirements :-
Python 3.x
Libraries:
pip install pillow pandas yagmail

📝 Usage :-
1️⃣ Generate Certificates
Run the generator:
python certificate.py
Certificates will be saved inside generated_certificates/.
2️⃣ Send Certificates via Email
Edit send_emails.py to include your Gmail ID & App Password (⚠️ never commit your password).
Run:
python send_emails.py
Each student will automatically receive their certificate by email.
📊 Example CSV (students.csv)
Name,Roll_No,Branch,Hackathon,Date,Topic,Email
Tammana Sri Lakshmi Vasanthi,23B21A4202,CSE,AI Hackathon,20-08-2025,AI Chatbot,vasanthi@example.com
Ravi Kumar,23B21A4203,ECE,AI Hackathon,20-08-2025,Face Recognition,ravi@example.com

🏆 Output :-
✅ Certificates are automatically generated with:
Participant’s details
Principal’s name & designation
Signature in a stylish font
Emailed directly to students

🖼️ Sample Output Screenshot :-
Here is an example of a generated certificate:
![alt text](TAMMANA_SRI_LAKSHMI_VASANTHI_certificate.png)
![alt text](yandapalli_sai_varshitha_certificate.png)

👩‍💻 Author :-
Tammana Sri Lakshmi Vasanthi
(Computer Science Engineer, AI/ML Enthusiast)