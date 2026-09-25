import os
import qrcode

BASE_URL = "https://tech-xtract-s-smart-icards.vercel.app"

QR_FOLDER = "qrcodes"

new_members = [
    "TXT_GNRL_SECR_Sachin_Gautam.html",
    "TXT_VICE_PRESIDENT_Yaniya.html",
    "TXT_PRESIDENT_HITESH_TYAGI.html"
]

os.makedirs(QR_FOLDER, exist_ok=True)

for file in new_members:
    member_url = f"{BASE_URL}/Members/{file}"

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(member_url)
    qr.make(fit=True)

    qr_image = qr.make_image()

    output_name = os.path.splitext(file)[0] + ".png"
    output_path = os.path.join(QR_FOLDER, output_name)

    qr_image.save(output_path)

    print(f"Generated: {output_name}")

print("Done!")