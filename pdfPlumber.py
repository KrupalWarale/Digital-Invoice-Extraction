
import pdfplumber  # Import pdfplumber for PDF table extraction

# Path to your PDF file
pdf_path = "abc.pdf"

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Loop through each page in the PDF
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"\n--- Page {page_number} ---")  # Print page number
        tables = page.extract_tables()  # Extract tables from the page

        if not tables:
            print("No tables found on this page.")  # No tables found
            continue

        # Loop through each table found
        for table_index, table in enumerate(tables, start=1):
            print(f"\nTable {table_index}:")  # Print table index
            for row in table:
                # Print row if it has any non-empty cell
                if any(cell is not None and str(cell).strip() != '' for cell in row):
                    print(row)
