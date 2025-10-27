# Digital Invoice Extraction - Project Analysis

This project organizes Python scripts for extracting and analyzing data from PDF invoices using various libraries. The workspace is structured for clarity and modularity:


## Folder Structure & Library Observations

- **beautifulsoup/**: XML parsing and extraction using BeautifulSoup. Good for post-processing PDF-to-XML outputs, flexible for custom tag navigation, but not for direct PDF parsing.
- **camelot/**: Table extraction from PDFs using Camelot. Works well for simple, clearly bordered tables; struggles with complex or unstructured layouts.
- **pdfminer/**: Text and layout extraction from PDFs using pdfminer. Powerful for low-level text and position extraction, but table detection requires custom logic.
- **pdfplumber/**: Table and coordinate extraction from PDFs using pdfplumber. Best for structured invoices and well-defined tables; easy to use and visualize, but less effective for highly unstructured documents.
- **pdfquery/**: PDF parsing using pdfquery. Useful for searching and extracting elements by PDF structure; good for rule-based extraction, but setup can be verbose.
- **pymupdf/**: PDF text and coordinate extraction using PyMuPDF (fitz). Fast and memory-efficient, supports advanced features like word-level bounding boxes; less built-in table support.
- **tabula/**: Table extraction from PDFs using tabula. Java-based backend, good for batch table extraction; works best with tabular data, but setup can be heavier.
- **hybrid/**: Scripts that combine two or more libraries for advanced extraction or analysis, useful for handling edge cases or combining strengths of different tools.

## Key Points
- All PDF files are available in each folder for testing and demonstration.
- Hybrid scripts are separated for clarity and multi-library analysis.
- No files remain in the root directory except this README.
- **pdfplumber works best for extracting tables and data from structured invoices.**

This structure supports easy navigation, testing, and extension for future invoice extraction tasks.