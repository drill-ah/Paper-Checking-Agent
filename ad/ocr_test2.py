from pdf2image import convert_from_path
from paddleocr import PaddleOCR
import os

PDF_PATH = r"E:\6 Semester\AD Samples\Sample4.pdf"
OUTPUT_TXT = r"E:\6 Semester\AD Samples\output.txt"
POPPLER_PATH = r"D:\Release-25.12.0-0\poppler-25.12.0\Library\bin"

ocr = PaddleOCR(lang="en")

pages = convert_from_path(
    PDF_PATH,
    dpi=300,
    poppler_path=POPPLER_PATH
)

print(f"Pages detected: {len(pages)}")

final_text = ""

for i, page in enumerate(pages, start=1):
    image_path = f"page_{i}.png"
    page.save(image_path, "PNG")

    # ✅ CORRECT FUNCTION CALL
    result = ocr.ocr(image_path)

    final_text += f"\n\n===== PAGE {i} =====\n"

    for line in result:
        for word in line:
            final_text += word[1][0] + " "

    os.remove(image_path)

with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write(final_text)

print("✅ OCR completed successfully")
