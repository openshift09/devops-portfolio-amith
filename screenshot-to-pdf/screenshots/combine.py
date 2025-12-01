import os
from PIL import Image
from datetime import datetime

input_folder = "screenshots"
output_folder = "pdfs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Collect all supported images
images = []
supported = (".png", ".jpg", ".jpeg")

for file in sorted(os.listdir(input_folder)):
    if file.lower().endswith(supported):
        images.append(os.path.join(input_folder, file))

if not images:
    print("No images found in screenshots/ folder.")
    exit()

# Load images
pil_images = []
for img in images:
    im = Image.open(img).convert("RGB")
    pil_images.append(im)

# Output PDF
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
pdf_path = f"{output_folder}/combined_{timestamp}.pdf"

first_img = pil_images[0]
rest = pil_images[1:]

first_img.save(pdf_path, save_all=True, append_images=rest)

print(f"PDF created successfully → {pdf_path}")
