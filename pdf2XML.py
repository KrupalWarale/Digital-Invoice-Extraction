
# Import BeautifulSoup for XML parsing
from bs4 import BeautifulSoup
# Import defaultdict for grouping
from collections import defaultdict

# Load the XML file from pdf2xml
with open("abc.xml", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "xml")

# Group words into rows using 'top' value
rows = defaultdict(list)

# Loop through each <text> tag in the XML
for text_tag in soup.find_all("text"):
    top = int(text_tag.get("top"))  # Get vertical position
    left = int(text_tag.get("left"))  # Get horizontal position
    text = text_tag.get_text().strip()  # Get text content
    if text:
        rows[top].append((left, text))  # Group by top

# Convert to list of lists, sorted by vertical (top) and then horizontal (left)
table = []
for top in sorted(rows.keys()):
    sorted_row = sorted(rows[top], key=lambda x: x[0])  # Sort by X
    row_values = [text for _, text in sorted_row]  # Get only text
    table.append(row_values)

# Print in Python list of lists format
print("[")  # Start of table
for row in table:
    print(f"  {row},")  # Print each row
print("]")  # End of table
