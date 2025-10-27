import os
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLineHorizontal, LTTextBoxHorizontal
from collections import defaultdict

def extract_pdfminer_coordinates(pdf_path):
    try:
        rows = defaultdict(list)
        for page_layout in extract_pages(pdf_path):
            for element in page_layout:
                if isinstance(element, (LTTextLineHorizontal, LTTextBoxHorizontal)):
                    # Process each text line or text box as a cell
                    for text_line in element if isinstance(element, LTTextBoxHorizontal) else [element]:
                        text_content = text_line.get_text().strip()
                        if text_content:
                            x0, y0, x1, y1 = text_line.bbox
                            rows[int(y0)].append((x0, x0, y0, x1, y1, text_content))
                elif isinstance(element, LTTextContainer):
                    # Fallback for other text containers, if any
                    for text_line in element:
                        if isinstance(text_line, LTTextLineHorizontal):
                            text_content = text_line.get_text().strip()
                            if text_content:
                                x0, y0, x1, y1 = text_line.bbox
                                rows[int(y0)].append((x0, x0, y0, x1, y1, text_content))
        
        output_lines = []
        if rows:
            for top_val in sorted(rows.keys(), reverse=True):
                sorted_row = sorted(rows[top_val], key=lambda x: x[0])
                row_coordinates = []
                for left, x0, y0, x1, y1, text_content in sorted_row:
                    row_coordinates.append(f"('{text_content}', {x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})")
                output_lines.append(f"[{', '.join(row_coordinates)}]")
        else:
            output_lines.append("No text elements found in the PDF file.")

        output_file = "pdfminer_coordinates_output.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for line in output_lines:
                f.write(line + '\n')
        print(f"Output written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pdf_file = "abc.pdf"
    extract_pdfminer_coordinates(pdf_file)