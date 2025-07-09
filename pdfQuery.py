
# Import PDFQuery for PDF parsing
from pdfquery import PDFQuery
# Import defaultdict for grouping
from collections import defaultdict

# Load the PDF file
pdf = PDFQuery('abc.pdf')
pdf.load()

# Group elements by Y-position (top alignment)
rows_by_y = defaultdict(list)

# Loop over all text elements in the PDF
for elem in pdf.pq('LTTextLineHorizontal'):
    text = elem.text.strip()  # Get text and remove spaces
    if not text:
        continue  # Skip empty text
    y = float(elem.attrib["y0"])  # Get Y position
    # Round Y to normalize nearby text lines (tolerance)
    rounded_y = round(y / 2) * 2
    rows_by_y[rounded_y].append((float(elem.attrib["x0"]), text))  # Group by Y

# Sort rows top to bottom and columns left to right
structured_rows = []
for y in sorted(rows_by_y.keys(), reverse=True):  # Top to bottom
    row = sorted(rows_by_y[y], key=lambda x: x[0])  # Left to right
    row_text = [text for _, text in row]  # Get only text
    structured_rows.append(row_text)

# Print each row cleanly
for row in structured_rows:
    print(row)
