"""
TechXtract Society - Automated QR Code Generator
Run this script to automatically generate QR codes for every HTML file in the Members/ folder.

Requirements:
    pip install qrcode pillow
"""

import os
import sys

try:
    import qrcode
except ImportError:
    print("qrcode library not found. Please install it by running:")
    print("pip install qrcode pillow")
    sys.exit(1)

# ==========================================
# CONFIGURATION
# ==========================================
# Change this to your deployed site URL (e.g. GitHub Pages)
# Example: "https://your-github-username.github.io/TechXtract-s-Smart-Icards"
BASE_URL = "https://your-domain.com"

MEMBERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Members")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qrcodes")

# ==========================================
# GENERATION LOGIC
# ==========================================
def generate_all_qrs():
    if not os.path.exists(MEMBERS_DIR):
        print(f"Error: Members directory not found at {MEMBERS_DIR}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    html_files = [f for f in os.listdir(MEMBERS_DIR) if f.endswith(".html")]
    if not html_files:
        print("No HTML files found in Members directory.")
        return

    print(f"Found {len(html_files)} member HTML files.")
    print(f"Generating QR codes using Base URL: {BASE_URL}")

    count = 0
    for filename in sorted(html_files):
        # Target URL when scanned
        target_url = f"{BASE_URL.rstrip('/')}/Members/{filename}"

        # Create QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(target_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image with same name as member file (PNG format)
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        img.save(output_path)
        count += 1

    print(f"Success! Generated {count} QR codes in: {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_all_qrs()
