import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# --- Configuration ---
CERTIFICATE_TEMPLATE_PATH = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/template.png"
PARTICIPANTS_FILE_PATH = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/students.csv"
OUTPUT_DIR = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/generated_certificates"

FONT_PATH_REGULAR = r"C:/Windows/Fonts/arial.ttf"
FONT_SIZE_BODY = 50
SIGNATURE_FONT_PATH = r"C:/Users/VASANTHI/OneDrive/Desktop/certificate/signature_font.ttf"

TEXT_BOUNDS = {
    "body_text": (180, 540, 1800, 1000)
}

DEBUG_MODE = False

# ----------------- Helper Functions -----------------
def load_font(path, size):
    return ImageFont.truetype(path, size)


def draw_paragraph(draw, text, box, font_path, max_size):
    x1, y1, x2, y2 = box
    box_width = x2 - x1
    box_height = y2 - y1

    font_size = max_size
    while font_size > 10:
        font = load_font(font_path, font_size)
        words = text.split()
        lines, current_line = [], ""
        for word in words:
            test_line = (current_line + " " + word).strip()
            w, _ = draw.textbbox((0, 0), test_line, font=font)[2:]
            if w <= box_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)

        total_height = len(lines) * int(font_size * 1.2)
        if total_height <= box_height:
            break
        font_size -= 2

    y_offset = y1 
    for line in lines:
        w, _ = draw.textbbox((0, 0), line, font=font)[2:]
        x_offset = x1 + (box_width - w) / 2
        draw.text((x_offset, y_offset), line, font=font, fill=(0, 0, 0))
        y_offset += int(font_size * 1.4)
def generate_certificate(participant_data):
    name = str(participant_data["Name"])
    Roll_No = str(participant_data["Roll_No"])
    date = participant_data["Date"]
    branch = str(participant_data["Branch"])
    topic = str(participant_data["topic"])
    hackathon_name = str(participant_data["Hackathon_Name"])

    if isinstance(date, pd.Timestamp):
        date = date.strftime("%Y-%m-%d")

    try:
        img = Image.open(CERTIFICATE_TEMPLATE_PATH).convert("RGB")
        draw = ImageDraw.Draw(img)

        if DEBUG_MODE:
            draw.rectangle(TEXT_BOUNDS["body_text"], outline="red", width=3)

        body_text = (
            f"This is to certify that {name}, Roll No: {Roll_No}, of the {branch} department "
            f"has successfully participated in the {hackathon_name} held on {date}. "
            f"The student presented a project on \"{topic},\" showcasing innovation, "
            "creativity, and technical skills. We appreciate their dedication, teamwork, "
            "and enthusiasm in making the event a success."
        )

        draw_paragraph(draw, body_text, TEXT_BOUNDS["body_text"], FONT_PATH_REGULAR, FONT_SIZE_BODY)
         # --- Add Signature (Revathi Duba) in signature font ---
        signature_text = "Revathi Duba"
        signature_font = load_font(SIGNATURE_FONT_PATH, 70)  # signature-style font
        sig_w, sig_h = draw.textbbox((0, 0), signature_text, font=signature_font)[2:]
        sig_x = (img.width - sig_w) / 2
        sig_y = img.height - 300  # position above designation
        draw.text((sig_x, sig_y), signature_text, font=signature_font, fill=(0, 0, 0))
        signature_font = load_font(SIGNATURE_FONT_PATH, 70)

        # --- Add Principal Name at the bottom ---
        principal_text = "Prof. Revathi Duba\nPrincipal"
        principal_font = load_font(FONT_PATH_REGULAR, 40)
        w, h = draw.textbbox((0, 0), principal_text, font=principal_font)[2:]
        x = (img.width - w) / 2
        y = img.height - 200  # push up from bottom
        draw.multiline_text(
            (x, y),
            principal_text,
            font=principal_font,
            fill=(0, 0, 0),
            align="center",
            spacing=20  # adds space between name & designation
        )

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        output_filename = f"{name.replace(' ', '_')}_certificate.png"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        img.save(output_path)
        print(f"✅ Generated certificate for {name} -> {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error generating certificate for {name}: {e}")
        return None

def main():
    if not os.path.exists(PARTICIPANTS_FILE_PATH):
        print("❌ Participant list not found.")
        return

    if not os.path.exists(CERTIFICATE_TEMPLATE_PATH):
        print("❌ Certificate template not found.")
        return

    df = pd.read_csv(PARTICIPANTS_FILE_PATH, encoding="latin1")
    for index, row in df.iterrows():
        print(f"\n➡ Processing entry {index + 1}: {row['Name']}")
        generate_certificate(row)

if __name__ == "__main__":
   main()
