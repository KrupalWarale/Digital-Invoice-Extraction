
# Import extract_pages to get layout of each page
from pdfminer.high_level import extract_pages
# Import LTTextContainer to identify text elements
from pdfminer.layout import LTTextContainer

# Loop through each page's layout in the PDF
for page_layout in extract_pages("abc.pdf"):
    # Loop through each element in the page layout
    for element in page_layout:
        # Check if the element is a text container
        if isinstance(element, LTTextContainer):
            # Print the text content of the element
            print(element.get_text())
