import pytesseract
from pdf2image import convert_from_path
from pathlib import Path
import os

PDF_PATH = Path(r"E:\6 Semester\AD Samples\Sample4.pdf")
POPPLER_PATH = r"D:\Release-25.12.0-0\poppler-25.12.0\Library\bin"   

    
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


OUTPUT_TXT = PDF_PATH.with_suffix(".txt")


pages = convert_from_path(
    pdf_path=str(PDF_PATH),
    dpi=300,
    poppler_path=POPPLER_PATH
)

print(f"Pages detected: {len(pages)}")


final_text = ""

for i, page in enumerate(pages, start=1):
    text = pytesseract.image_to_string(page, lang="eng")
    final_text += f"\n\n===== PAGE {i} =====\n{text}"


with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    f.write(final_text)

print("✅ OCR completed using Tesseract")
print("📄 Output saved at:", OUTPUT_TXT)
