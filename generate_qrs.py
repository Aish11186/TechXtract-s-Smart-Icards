import os
import qrcode

# Deployed website URL
BASE_URL = "https://tech-xtract-s-smart-icards.vercel.app"

# Folder containing member HTML files
MEMBERS_FOLDER = "Members"

# Folder where QR codes will be saved
QR_FOLDER = "qrcodes"

# Create qrcodes folder if it doesn't exist
os.makedirs(QR_FOLDER, exist_ok=True)

# Get all HTML files from Members folder
member_files = [
    file for file in os.listdir(MEMBERS_FOLDER)
    if file.endswith(".html")
]

print(f"Found {len(member_files)} member pages.")

for file in member_files:

    # Create URL for this member
    member_url = f"{BASE_URL}/Members/{file}"

    # Create QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(member_url)
    qr.make(fit=True)

    # Generate QR image
    qr_image = qr.make_image()

    # Same filename, but .png
    output_name = os.path.splitext(file)[0] + ".png"
    output_path = os.path.join(QR_FOLDER, output_name)

    qr_image.save(output_path)

    print(f"Generated: {output_name}")

print("\nDone!")
print(f"QR codes saved in: {QR_FOLDER}/")
