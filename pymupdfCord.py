import fitz  # PyMuPDF
from collections import defaultdict

def extract_pymupdf_coordinates(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        rows = defaultdict(list)

        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            words = page.get_text("words")  # Extract words with their bounding boxes
            
            # Group words into lines based on their top (y0) coordinate
            # A small tolerance is used to group words that are on the same visual line
            line_tolerance = 3 # Adjust as needed
            temp_lines = defaultdict(list)

            for word_info in words:
                x0, y0, x1, y1, text_content, block_no, line_no, word_no = word_info
                if text_content.strip():
                    # Find an existing line or start a new one
                    found_line = False
                    for line_y in temp_lines.keys():
                        if abs(line_y - y0) <= line_tolerance:
                            temp_lines[line_y].append((x0, y0, x1, y1, text_content))
                            found_line = True
                            break
                    if not found_line:
                        temp_lines[y0].append((x0, y0, x1, y1, text_content))

            # Process each identified line
            for line_y in sorted(temp_lines.keys(), reverse=True):
                sorted_words_in_line = sorted(temp_lines[line_y], key=lambda x: x[0])
                
                # Combine words to form the full line text and calculate the bounding box for the line
                full_line_text = []
                line_x0 = float('inf')
                line_y0 = float('inf')
                line_x1 = float('-inf')
                line_y1 = float('-inf')

                for x0_word, y0_word, x1_word, y1_word, text_content in sorted_words_in_line:
                    full_line_text.append(text_content)
                    line_x0 = min(line_x0, x0_word)
                    line_y0 = min(line_y0, y0_word)
                    line_x1 = max(line_x1, x1_word)
                    line_y1 = max(line_y1, y1_word)
                
                if full_line_text:
                    rows[int(line_y0)].append((line_x0, line_y0, line_x1, line_y1, " ".join(full_line_text)))

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

        output_file = "pymupdf_coordinates_output.txt"
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
    extract_pymupdf_coordinates(pdf_file)