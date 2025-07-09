doc = fitz.open("abc.pdf")

import fitz  # Import PyMuPDF for PDF processing

# Open the PDF file
doc = fitz.open("abc.pdf")
# Loop through each page in the PDF
for page_number, page in enumerate(doc, start=1):
    print(f"\n--- Page {page_number} ---")  # Print page number
    blocks = page.get_text("dict")["blocks"]  # Get text blocks
    for block in blocks:
        for line in block.get("lines", []):  # Loop through lines in block
            # Join all text spans in the line
            text_line = " | ".join(span["text"] for span in line["spans"])
            print(text_line)  # Print the line
