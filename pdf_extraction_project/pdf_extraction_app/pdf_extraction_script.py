from PyPDF2 import PdfReader
import re
from datetime import datetime

def extract_data_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    
    patterns = {
        "Invoice Number": r"Invoice\s*Number:\s*(\w+)",
        "Date": r"Date:\s*(\d{4}-\d{2}-\d{2})",
        "Total Amount": r"Total\s*Amount:\s*\$?(\d+(\.\d{1,2})?)"
    }

    extracted_data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            extracted_data[key] = match.group(1)
    
    extracted_date = extracted_data.get("Date", datetime.now().strftime("%Y-%m-%d"))
    extracted_data["Date"] = extracted_date

    return extracted_data
